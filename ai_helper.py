import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_summary(role, skills):
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Write a professional resume summary.

    Role: {role}
    Skills: {skills}

    Keep it under 80 words.
    """

    response = model.generate_content(prompt)

    return response.text