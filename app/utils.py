import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_documents_from_folder(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith('.txt'):
            loader = TextLoader(full_path)
        elif file.endswith('.pdf'):
            loader = PyPDFLoader(full_path)
        else:
            continue
        docs.extend(loader.load())
    return docs
