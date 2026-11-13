import os
import sys

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from services.document_loader import load_documents
from services.vector_store import create_vector_store

documents = load_documents(
    ["documents/HR_Policy.pdf"]
)

create_vector_store(documents)

print("Done")