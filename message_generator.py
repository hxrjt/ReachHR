import os
import openai
from dotenv import load_dotenv

load_dotenv()
openAI_key=os.getenv("OPENAI_API_KEY")

def generate_cold_message(company,user_prompt):
    """
    Generate a cold LinkedIn message using company name and user-defined prompt.

    Args:
        company (str): Company name
        user_prompt (str): Purpose of cold message (e.g. ask for internship, referral, etc.)

    Returns:
        str: AI-generated cold message
    """
    prompt = f"""
    You are an expert at writing effective, human-sounding cold messages on LinkedIn.

    Task:
    Write a cold message addressed to someone at {company}.
    The user's information and goal is: {user_prompt}

    Guidelines:
    - Keep it precise and good.
    - Be polite, professional, and conversational.
    - Do not sound robotic or overly formal.
    - This message should be usable in a LinkedIn DM.
    - The message sould be 7-8 lines such that the person can send their CV after the message

    Write the message now:
    """
    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            temperature=0.7,
            max_tokens=400
        )
        return response["choices"][0]["message"]["content"].strip()
    
    except Exception as e:
        return f"❌ Error generating message: {str(e)}"