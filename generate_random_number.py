import secrets

def generate_random_number(entropy):
    entropy_bytes = int(entropy)  # converting entropyt to int 
    entropy_bytes = min(entropy_bytes, 32)  # 32bytes for max entropy

    secrets.token_hex(entropy_bytes)

    random_number = secrets.randbelow(10**6)

    return random_number
