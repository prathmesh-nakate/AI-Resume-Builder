import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_summary(role, skills):
    prompt = f"""
    Write a professional resume summary.

    Role: {role}
    Skills: {skills}

    Keep it under 80 words.
    """

    response = model.generate_content(prompt)

    return response.text