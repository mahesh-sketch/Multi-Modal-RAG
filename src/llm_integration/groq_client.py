import sys
from langchain_groq import ChatGroq
from configs.settings import settings
from core.exception import CustomException
from core.logger import logging

def get_groq_client(model_name: str = "meta-llama/llama-4-maverick-17b-128e-instruct", temperature: float = 0.5):
    """
    Initialize Groq model using LangChain wrapper.

    Args:
        model_name (str): The Groq model version to use.
        temperature (float): Temperature setting for output creativity.

    Returns:
        ChatGroq: Initialized model instance.
    """
    try:
        if not settings.GROQ_API_KEY:
            raise CustomException("GROQ_API_KEY is not set in the environment variables.")
        
        logging.info(f"Initializing Groq client with model: {model_name} and temperature: {temperature}")
        
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=model_name,
            temperature=temperature,
        )
    except Exception as e:
        logging.error(f"Failed to initialize Groq client: {e}")
        raise CustomException(e, sys)