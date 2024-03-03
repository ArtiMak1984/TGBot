import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")

TOKEN_OPENAI = os.getenv("TOKEN_OPENAI")