import os

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_documents():

    loader = DirectoryLoader(
        "data",
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    return chunks
def create_vector_store(chunks):

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS vector database...")

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_db.save_local("vector_db")

    print("✅ Vector database saved successfully!")


if __name__ == "__main__":

    docs = load_documents()

    chunks = split_documents(docs)
    create_vector_store(chunks)