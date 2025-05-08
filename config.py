import os
from dotenv import load_dotenv

load_dotenv()


# Retrieve api key from environment variables
def get_openai_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return key


Model = "gpt-4"
