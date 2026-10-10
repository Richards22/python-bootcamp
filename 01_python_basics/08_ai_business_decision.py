import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

business_info = """
Business Name: Fitsquare ltd
Monthly Revenue: $50,000
Years in business: 4
Requested loan: $10,000
"""

prompt = f"""
You are a business loan pre-screening assistant.

Review the following information:

{business_info}

Give a simple preliminary assessment.

Return exactly three things:
1. Decision: Pre-Qualified, Needs more information, or Likely Declined
2. Reason: one sentence
3. Missing information: list any important information that is missing
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content":prompt
        }
    ]
)

result = response.choices[0].message.content
print(result)