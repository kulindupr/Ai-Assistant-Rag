import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from app.config import GEMINI_API_KEY
from app.dependencies import get_vectorstore
import logging
import traceback

logger = logging.getLogger(__name__)

genai.configure(api_key=GEMINI_API_KEY)

def get_embedding(text):
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_document"
        )
        return result['embedding']
    except Exception as e:
        logger.error(f"Error getting embedding: {str(e)}")
        raise

def answer_question(question: str):
    try:
        logger.info(f"Received question: {question}")
        
        # Load the FAISS index
        logger.info("Loading FAISS index")
        db = get_vectorstore()
        
        # Search for relevant documents
        logger.info("Searching for relevant documents")
        docs = db.similarity_search(question, k=3)
        logger.info(f"Found {len(docs)} relevant documents")
        
        # Generate answer using Gemini
        logger.info("Generating answer using Gemini")
        model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"""Based on the following context, please answer the question. If the answer cannot be found in the context, say "I don't have enough information to answer that question."

Context:
{context}


Question: {question}

Answer:"""
        
        logger.info("Sending request to Gemini")
        response = model.generate_content(prompt)
        logger.info("Received response from Gemini")
        
        if not response.text:
            raise Exception("Empty response from Gemini")
            
        return response.text
    except Exception as e:
        logger.error(f"Error answering question: {str(e)}")
        logger.error(traceback.format_exc())
        raise
