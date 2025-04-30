from app.utils import load_documents_from_folder
from app.config import GEMINI_API_KEY
from langchain_community.vectorstores import FAISS
import google.generativeai as genai
from langchain_core.embeddings import Embeddings
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

genai.configure(api_key=GEMINI_API_KEY)

class GeminiEmbeddings(Embeddings):
    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=text,
                task_type="retrieval_document"
            )
            embeddings.append(result['embedding'])
        return embeddings

    def embed_query(self, text):
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_query"
        )
        return result['embedding']

def load_vectorstore():
    try:
        logger.info("Loading documents from data/documents")
        docs = load_documents_from_folder("data/documents")
        logger.info(f"Loaded {len(docs)} documents")
        
        logger.info("Creating embeddings")
        embeddings = GeminiEmbeddings()
        
        logger.info("Creating FAISS index")
        db = FAISS.from_documents(docs, embeddings)
        
        logger.info("Saving FAISS index")
        db.save_local("vectorstore/faiss_index")
        logger.info("Vectorstore created successfully")
    except Exception as e:
        logger.error(f"Error creating vectorstore: {str(e)}")
        raise

def get_vectorstore():
    """Load the vectorstore with safe deserialization"""
    try:
        logger.info("Loading FAISS index")
        embeddings = GeminiEmbeddings()
        db = FAISS.load_local(
            "vectorstore/faiss_index",
            embeddings,
            allow_dangerous_deserialization=True  # Safe since we created the index
        )
        logger.info("FAISS index loaded successfully")
        return db
    except Exception as e:
        logger.error(f"Error loading vectorstore: {str(e)}")
        raise
