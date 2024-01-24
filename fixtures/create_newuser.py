import json

import requests
from apiautomation.common.application import baseUrl, urlParams

# url = "https://reqres.in/api/users"
createuser_url = baseUrl().format(urlParams()["create_user"])
# str(baseUrl()) + format(urlParams()["create_user"])


def createuser():
    # global response_received
    createuser_file = open("/usr/local/google/home/sateeshg/createuser.json", "r")
    for line in createuser_file:
        input_json_format = json.loads(line)
        print("Converted input to json format: ", input_json_format)
        post_response = requests.post(createuser_url, input_json_format)
        print("Received Status Code: ", post_response.status_code)
        assert post_response.status_code == 201, "Status Code Failed"
        response_received = json.loads(post_response.text)
        print("Response Received: ", response_received)
        print("Job from the response received: ", response_received['job'])
        print("------------------------------")
        if response_received['job'] == "QAleader Updated":
            print("Job Matched")
            break
    return response_received['job']


expected_job = "QAleader Updated"
assert createuser().casefold() == expected_job.casefold(), "Job Match Failed"
