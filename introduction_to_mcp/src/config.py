from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "deepseek-chat")
    DOCUMENT_ROOT = os.getenv("DOCUMENT_ROOT", "documents")


settings = Settings()
