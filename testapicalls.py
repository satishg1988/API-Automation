import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
response_data = response.json()
print("response received:", response_data)
print("Status Code: ", response.status_code)
assert response.status_code == 200, "Status Failed"
for data in response_data:
    print("Title From Response: ", data['title'])
    if data['title'] == 'qui est esse':
        print("Found Title : ", data['title'])
        break
