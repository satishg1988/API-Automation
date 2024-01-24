import json

import requests

url = "https://reqres.in/api/users/2"
response_received_del = requests.delete(url)
print("Response Received From  Del: ", response_received_del)
actual_statuscode_del = response_received_del.status_code
expected_statuscode = 204
assert actual_statuscode_del == expected_statuscode, "Delete Request Status Code Verification Failed"
