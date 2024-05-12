import numpy as np

def extract_entropy(audio_data):
    entropy = np.std(audio_data)
    return entropy
