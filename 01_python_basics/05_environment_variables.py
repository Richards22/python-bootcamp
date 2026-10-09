import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("MY_API_KEY")

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


data = {

    "title": "Environmental Variables",
    "body": "Practicing API authentication with Python",
    "userid": 1
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

print("Status code:", response.status_code)

if response.status_code ==201:
    result = response.json()
    print("Request Successful!")
    print("Post ID:", result["id"])
    print("Title:", result["title"])
else:
    print("Request failed:", response.text)



