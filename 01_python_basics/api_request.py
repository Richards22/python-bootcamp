"""
First API request
Learning project for AI Automation Engineer Bootcamp.

Purpose:
Learn how Python communicates with an API
and processes a JSON response.
"""

import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print("API Response:")
print(data)

print("\nTask title:", data['title'])
print("Completed:", data['completed'])