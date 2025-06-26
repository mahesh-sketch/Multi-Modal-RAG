import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from configs.settings import settings
from core.exception import CustomException
from core.logger import logging


def get_genai_client(model_name:str="gemini-2.0-flash", temperature: float = 0.5):
    """
    Initialize Google Generative AI model using LangChain wrapper.

    Args:
        model_name (str): The Gemini model version to use.
        temperature (float): Temperature setting for output creativity.

    Returns:
        ChatGoogleGenerativeAI: Initialized model instance.
    """
    try:
        if not settings.GOOGLE_API_KEY:
            raise CustomException("GOOGLE_API_KEY is not set in the environment variables.")
        
        logging.info(f"Initializing Google Generative AI client with model: {model_name} and temperature: {temperature}")
        
        return ChatGoogleGenerativeAI(
            api_key=settings.GOOGLE_API_KEY,
            model=model_name,
            temperature=temperature,
        )
    except Exception as e:
        logging.error(f"Failed to initialize Google Generative AI client: {e}")
        raise CustomException(e, sys)
    
model = get_genai_client()
print(model.invoke("Hello, how are you?").content)  # Example usage to test the client
