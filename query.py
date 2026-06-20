import json
from llama_cpp import Llama

# Load chunks
with open(
    "data/processed/sections.json",
    "r",
    encoding="utf-8"
) as f:
    sections = json.load(f)

# Load model
llm = Llama(
    model_path="models/qwen2.5-3b-instruct-q5.gguf",
    n_ctx=4096,
    n_threads=8,
    verbose=False
)

def retrieve(query):
    query_words = query.lower().split()

    scores = []

    for section in sections:
        text = section["content"].lower()

        score = sum(
            word in text
            for word in query_words
        )

        scores.append(
            (score, section["content"])
        )

    scores.sort(reverse=True)

    return scores[0][1]


while True:
    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    context = retrieve(question)

    prompt = f"""
Use the document context below to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm(
        prompt,
        max_tokens=300,
        temperature=0.2
    )

    print("\n")
    print(response["choices"][0]["text"])