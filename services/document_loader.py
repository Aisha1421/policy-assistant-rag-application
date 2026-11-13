from langchain_community.document_loaders import PyPDFLoader


def load_documents(pdf_paths):
    documents = []

    for pdf in pdf_paths:
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())

    return documents