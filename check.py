import openai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

models = openai.Model.list()
print([model.id for model in models["data"]])