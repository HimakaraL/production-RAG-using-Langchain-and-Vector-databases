import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader)

def load_text_file():
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name

    # Load the text file using TextLoader
    loader = TextLoader(temp_file_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} documents(s)")
    print(f"Content preview: {documents[0].page_content[:100]}")
    print(f"Metadata: {documents[0].metadata}")

    # Print the loaded documents
    # for doc in documents:
    #     print(doc)

    # Clean up the temporary file
    os.remove(temp_file_path)

def pdf_loader(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s) from PDF.")
    for i, doc in enumerate(documents):
        print(f"Document {i + 1}:- Page Content:{doc.page_content[:100]}... Metadata: {doc.metadata}")

if __name__ == "__main__":
    pdf_loader("./docs/IT22550262_StudentPerformanceProfile (1).pdf")