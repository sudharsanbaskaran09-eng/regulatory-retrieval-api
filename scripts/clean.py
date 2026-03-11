import os
import re

INPUT_FILE = "output/regulation.txt"
OUTPUT_FILE = "output/regulation_clean.txt"


def clean_text(text):
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove special characters except punctuation
    text = re.sub(r'[^\w\s.,;:!?()-]', '', text)

    # remove repeated punctuation
    text = re.sub(r'([.,;:!?])\1+', r'\1', text)

    return text.strip()


def main():
    if not os.path.exists(INPUT_FILE):
        print("Input text file not found.")
        return

    print("Cleaning extracted text...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned_text = clean_text(raw_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print("Cleaning complete.")
    print(f"Saved cleaned text to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()