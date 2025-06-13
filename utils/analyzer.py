from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_openai_feedback(resume_text, jd_text):
    prompt = f"""You are an HR assistant. Analyze the following resume and job description.

Resume:
{resume_text}

Job Description:
{jd_text}

Provide feedback on how well the resume matches the job, and suggest improvements.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an intelligent HR assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )
    return response.choices[0].message.content