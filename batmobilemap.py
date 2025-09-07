import base64
import hashlib
import random

chunks = [
    "U2VjcmV0S2V5PT0xMjM0NQ==",
    "Y29kZW5hbWU9dHJ1c2lz",
    "aWRfNDU2X2hlbGw=",
    "c2hhZG93X2FsbF9mb3JjZXM=",
    "bWlzc2luZ19jaGFpbnM=",
]

def scramble(data: str) -> str:
    """Scrambles a string into a fake hash."""
    return hashlib.sha256(data.encode()).hexdigest()

def reveal():
    """Pick a random chunk and scramble it like a hidden secret."""
    chosen = random.choice(chunks)
    decoded = base64.b64decode(chosen).decode()
    return scramble(decoded)

if __name__ == "__main__":
    print("🔒 Hidden file initialized...")
    for i in range(5):
        print(f"[{i}] {reveal()}")
