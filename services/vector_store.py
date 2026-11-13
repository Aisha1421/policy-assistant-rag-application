from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL
)


def create_vector_store(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )

    db = FAISS.from_documents(
        docs,
        embeddings
    )

    db.save_local("vector_store")

    print("Embedding Model:", EMBEDDING_MODEL)
    print("Vector Store Created Successfully!")