from llama_cpp import Llama

llm = Llama(
    model_path="models/qwen2.5-3b-instruct-q5.gguf",
    n_ctx=2048,
    n_threads=8,
    verbose=False
)

response = llm(
    "Q: What is Artificial Intelligence?\nA:",
    max_tokens=100
)

print(response["choices"][0]["text"])


