import json

import pytest
import requests

url = "https://reqres.in/api/users"


# @pytest.fixture(scope="class")
def outPutFromFileToJsonFormat():
    global postreq_response_received

    createuser_file = open("/usr/local/google/home/sateeshg/createuser", "r")
    output_from_file = createuser_file.read()
    print("Read input from the text file: ", output_from_file)
    output_json_format = json.loads(output_from_file)
    print("Converted input to json format: ", output_json_format)
    postreq_response_received = requests.post(url, output_json_format)
    return postreq_response_received
