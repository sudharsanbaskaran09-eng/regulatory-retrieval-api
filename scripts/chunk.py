import os
import json

INPUT_FILE = "output/regulation_clean.txt"
OUTPUT_FILE = "output/chunks.json"

CHUNK_SIZE = 200


def chunk_text(text, chunk_size):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def main():
    if not os.path.exists(INPUT_FILE):
        print("Cleaned text file not found.")
        return

    print("Creating text chunks...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text, CHUNK_SIZE)

    os.makedirs("output", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"Created {len(chunks)} chunks.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()