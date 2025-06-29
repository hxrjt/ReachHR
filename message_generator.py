import os
import cohere
from dotenv import load_dotenv


load_dotenv()
cohere_api_key = os.environ.get("COHERE_API_KEY")
co=cohere.Client(cohere_api_key)


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
    You are a cold message generating expert.

    Task:
    Write a cold message addressed to someone at {company} for an Internship.
    The user's information and goal is: {user_prompt}

    Guidelines:
    - Keep it precise and good.
    - Be polite and professional.
    - Do not sound robotic or overly formal.
    - This message should be usable in a LinkedIn DM.
    - The message sould be of appropriate length such that the person can send their CV after the message

    Write the message now:
    """
    try:
        response=co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"❌ Error generating message: {str(e)}"