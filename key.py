import secrets

def generate_api_key():
    return secrets.token_hex(32)

api_key_1 = generate_api_key()
api_key_2 = generate_api_key()

with open('api_keys.txt', 'w') as file:
    file.write(f"API_KEY_1={api_key_1}\n")
    file.write(f"API_KEY_2={api_key_2}\n")