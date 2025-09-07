import random
import string
from datetime import datetime

class CipherBox:
    def __init__(self, key=None):
        self.key = key or self._generate_key()

    def _generate_key(self, length=16):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def encrypt(self, text):
        return ''.join(chr((ord(c) + len(self.key)) % 126) for c in text)

    def decrypt(self, text):
        return ''.join(chr((ord(c) - len(self.key)) % 126) for c in text)


class SecretNote:
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] {self.message}"


def mystery_numbers(seed=42):
    random.seed(seed)
    return [random.randint(1000, 9999) for _ in range(5)]


if __name__ == "__main__":
    cipher = CipherBox()
    note = SecretNote("The owl hoots at midnight.")
    encrypted = cipher.encrypt(note.message)
    decrypted = cipher.decrypt(encrypted)

    print("Generated Key:", cipher.key)
    print("Original:", note)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
    print("Mystery Numbers:", mystery_numbers())
