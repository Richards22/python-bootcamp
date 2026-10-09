import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

business_info = """
Business Name: Fitsquare ltd
Monthly Revenue: $3,000
Years in business: 0.5
Requested loan: $10,000
"""

prompt = f"""
You are a business loan pre-screening assistant.

Review this information:

{business_info}

Return ONLY valid JSON.
Do not use markdown.
Do not add any explanation outside the JSON.

The JSON must have excatly these fields:

{{
"decision": "Pre-Qualified, Needs more information, or Likely Declined",
"reason": "one sentence",
"missing_information": ["item 1", "item 2", "item 3"]
}}
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

ai_output = response.choices[0].message.content

result = json.loads(ai_output)

print("Decision:", result["decision"])
print("Reason:", result["reason"])
print("Missing Information:", result["missing_information"])

if result["decision"] == "Pre-Qualified":
    print("ACTION: Send application for further review.")

elif result["decision"] == "Needs more information":
    print("ACTION: Request additional information.")

elif result["decision"] == "Likely Declined":
    print("ACTION: Do not proceed with application.")

else:
    print("ACTION: Unknown decision. manual review required.")