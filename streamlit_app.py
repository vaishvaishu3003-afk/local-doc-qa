import streamlit as st
import json
from groq import Groq

st.set_page_config(
    page_title="Local Document Q&A",
    page_icon="📄"
)

st.title("📄 Document Q&A")

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

with open(
    "data/processed/sections.json",
    "r",
    encoding="utf-8"
) as f:
    sections = json.load(f)

def retrieve(query):
    query_words = query.lower().split()

    best_score = -1
    best_chunk = ""

    for section in sections:
        text = section["content"].lower()

        score = sum(
            word in text
            for word in query_words
        )

        if score > best_score:
            best_score = score
            best_chunk = section["content"]

    return best_chunk

question = st.text_input(
    "Ask a question about your PDF"
)

if question:

    context = retrieve(question)

    prompt = f"""
Use the document context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved Context"):
        st.write(context)