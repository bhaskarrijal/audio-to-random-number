import pyaudio
import numpy as np
import os
import soundfile as sf

def capture_audio(duration=5.0, rate=44100, channels=1):
    print("Starting audio capture...")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=1024)
    audio_data = []

    frames_to_capture = int(rate * duration / 1024)

    for _ in range(frames_to_capture):
        audio_data.append(stream.read(1024))

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.frombuffer(b''.join(audio_data), dtype=np.int16)
    audio_data = audio_data / np.iinfo(np.int16).max

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'captured_audio.wav')

    sf.write(file_path, audio_data, rate)

    print(f"Audio capture complete. Duration: {duration} seconds. Audio saved to {file_path}")
    return audio_data