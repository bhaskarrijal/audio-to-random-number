from capture_audio import capture_audio
from extract_entropy import extract_entropy
from generate_random_number import generate_random_number


def main():
    audio_data = capture_audio(duration=3.0)
    entropy = extract_entropy(audio_data)
    random_number = generate_random_number(entropy)
    print(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()