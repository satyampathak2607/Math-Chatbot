import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=".env")  
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set API key correctly
openai.api_key = OPENAI_API_KEY  

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Math Chatbot API!"}

@app.get("/ask")
def ask_question(query: str):
    try:
        response = openai.ChatCompletion.create(  # Use openai.ChatCompletion.create correctly
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Explain this math concept in simple terms: {query}"}]  
        )
        return {"answer": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


