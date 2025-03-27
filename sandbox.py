import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate(text: str):
    genai.configure(api_key=os.environ.get("GEMINI_KEY"))

    model = genai.GenerativeModel("gemini-1.5-flash")  # use correct available model name

    generation_config = genai.GenerationConfig(
        temperature=1.0,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    response = model.generate_content(
        contents=text,
        generation_config=generation_config,
        stream=True,
    )

    for chunk in response:
        print(chunk.text, end="")


