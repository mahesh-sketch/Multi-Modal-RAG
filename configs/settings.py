# Configuration settings for the application
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from core.exception import CustomException

# Load environment variables from .env file
load_dotenv()

class Settings:
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

    # Ensure the environment variables are set
    if not GOOGLE_API_KEY or not GROQ_API_KEY:
        raise CustomException("Missing required environment variables: GOOGLE_API_KEY and/or GROQ_API_KEY")
    
    
settings = Settings()