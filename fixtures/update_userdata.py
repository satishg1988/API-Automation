import json

import requests

url = "https://reqres.in/api/users/2"
update_user_file = open("/usr/local/google/home/sateeshg/createuser", "r")
content_update_user_file = update_user_file.read()
print("Content on update user file: ", content_update_user_file)
content_json_format = json.loads(content_update_user_file)
print("Content converted to json format: ", content_json_format)
response_from_putrequest = requests.put(url, content_json_format)
response_code_fromputrequest = response_from_putrequest.status_code
print("Response from put request: ", response_from_putrequest)
print("Response code received from put request: ", response_code_fromputrequest)
assert response_code_fromputrequest == 200, "Status Code Match Failed"
response_content_putrequest = json.loads(response_from_putrequest.text)
print("Response content received from put request: ", response_content_putrequest)
print("Name from  the update user file: ", content_json_format['name'])
print("Name from the response: ", response_content_putrequest['name'])
expected_name = "Maximus Updateddd"
assert response_content_putrequest['name'].lower() == expected_name.lower(), "Name Match Failed"
