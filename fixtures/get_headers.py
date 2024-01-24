import requests

url = "https://httpbin.org/get"
# api/users/2
headers_data = {'stu_id': 11282023, 'Grade': 'A+'}
response_received = requests.get(url, params=headers_data)
print("Response received: ", response_received.headers)
