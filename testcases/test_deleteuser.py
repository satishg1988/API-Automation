import requests

from apiautomation.common.application import baseUrl, urlParams

del_user_url = baseUrl().format(urlParams()["delete_user"])


def test_deleteUser():
    response = requests.delete(del_user_url)
    print("Response from del use rrequest:", response)
    print("Text From The Dele Request", response.text)
    assert response.status_code == 204, "Delete User: Status Code Didnt Matched"
