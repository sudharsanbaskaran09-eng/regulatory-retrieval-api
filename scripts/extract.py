import os
from pypdf import PdfReader

INPUT_PDF = "data/regulation.pdf"
OUTPUT_TEXT = "output/regulation.txt"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def save_text(text, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if not os.path.exists(INPUT_PDF):
        print("PDF file not found in data folder.")
        return

    print("Extracting text from PDF...")

    text = extract_text_from_pdf(INPUT_PDF)

    save_text(text, OUTPUT_TEXT)

    print("Extraction complete.")
    print(f"Saved to {OUTPUT_TEXT}")


if __name__ == "__main__":
    main()