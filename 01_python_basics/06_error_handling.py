import requests

url = "https://jsonplaceholder.typicode.com/posts"

data ={
    "title": "Error Handling",
    "body": "Learning how to handle API errors",
    "userid": 1
}

try:
    response = requests.post(url,json=data)

    response.raise_for_status()

    result = response.json()

    print("Request Successful!")
    print("Status code:", response.status_code)
    print("Post ID:", result["id"])

except requests.exceptions.RequestException as error:
    print("API request failed:")
    print("Error:", error)