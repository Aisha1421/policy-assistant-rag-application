from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

from langchain_community.vectorstores import FAISS

from config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL,
    EMBEDDING_MODEL,
)

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GOOGLE_API_KEY,
)

db = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True,
)

print("LLM Model:", "gemini-3.8-flash")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY,
)

def ask_question(question):
    docs = db.similarity_search(question, k=4)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a Policy Assistant.

Context:
{context}

Question:
{question}

Answer only from the provided context.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            doc.metadata.get("source")
            for doc in docs
        ]
    }