import requests

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = {
    "title": "AI Automation",
    "body": "Learning Python API automation with requests",
    "userId": 1
}

response = requests.post(
    url,
    headers=headers,
    json=data
)


print("Status Code:", response.status_code)

if response.status_code == 201:
    result = response.json()

    print("Request successful!")
    print("Post ID:", result['id'])
    print("Title:", result['title'])

else:
    print("Request failed!")
    print("Response:", response.text)
    