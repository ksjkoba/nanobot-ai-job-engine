import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from a .env file (for security)
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def tailor_resume_content(job_description, user_profile):
    \"\"\"
    Uses Gemini to extract key skills from a JD and 
    align them with your IAM/Saviynt background.
    \"\"\"
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f\"\"\"
    I am applying for a job with the following description:
    {job_description}

    My profile: {user_profile}

    Identify the top 3 technical requirements and explain how my 
    experience in Saviynt and Identity Management fits them perfectly.
    \"\"\"
    
    response = model.generate_content(prompt)
    return response.text
