import json

import jsonpath
import requests

from apiautomation.common.application import baseUrl, urlParams
url_getusers = baseUrl().format(urlParams()["get_users_list"])

def test_getHeadersData():
    response = requests.post(url_getusers)
    print("Response: ", response)
    received_headers = response.headers
    print("Headers Data: ", received_headers)
    print("Text Received From Response:", json.loads(response.text))

    assert json.loads(response.text)['id'].isnumeric(), "Failed: Data is not numeric"
    assert str(json.loads(response.text)['id'])
