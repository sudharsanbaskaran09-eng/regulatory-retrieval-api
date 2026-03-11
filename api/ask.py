import json
import os

CHUNKS_FILE = "output/chunks.json"


def load_chunks():
    if not os.path.exists(CHUNKS_FILE):
        print("Chunks file not found.")
        return []

    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    return chunks


def search_chunks(question, chunks):
    question_words = question.lower().split()

    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        score = 0
        chunk_lower = chunk.lower()

        for word in question_words:
            if word in chunk_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk


def ask_question(question):
    chunks = load_chunks()

    if not chunks:
        return "No chunks available."

    answer = search_chunks(question, chunks)

    if answer:
        return answer
    else:
        return "No relevant information found."


if __name__ == "__main__":
    question = input("Ask a question: ")

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)