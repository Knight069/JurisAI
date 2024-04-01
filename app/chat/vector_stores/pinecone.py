import os
from pinecone import Pinecone, ServerlessSpec
from app.chat.embeddings.openai import embeddings

from langchain_pinecone import PineconeVectorStore


vector_store = PineconeVectorStore(index_name=os.getenv("PINECONE_INDEX_NAME"), embedding= embeddings)


def build_retriever(chat_args, k):
    search_kwargs = {
        "filter": { "pdf_id": chat_args.pdf_id },
        "k": k
    }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )