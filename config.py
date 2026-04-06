import os 
from dotenv import load_dotenv

load_dotenv()

groqAPIkey = os.getenv("GROQ_API_KEY")
modelName = "llama-3.3-70b-versatile"
