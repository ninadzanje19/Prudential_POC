import google.generativeai as genai
import os
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("KEY_2")

# Configure Gemini API with the key
genai.configure(api_key=api_key)

def generate(prompt):
    #load the model
    model = genai.GenerativeModel("gemini-2.0-flash")  # Specify the model

    #generate a response
    response = model.generate_content(prompt)
    return response.text
