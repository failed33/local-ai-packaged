import secrets
import string

def generate_ascii_key(length=32):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    key = generate_ascii_key()
    print(f"Generated 32-character ASCII key:\n{key}")