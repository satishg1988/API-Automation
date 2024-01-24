import json

from common.endpoints import UserEndPoints
from fixtures.authentication import Auth


def test_validLoginUser(expected_status_code=200, expected_token="QpwL5tke4Pnpja7X4"):
    response = UserEndPoints().loginUser(data=Auth().valid())
    assert response.status_code == expected_status_code, "Valid Login User - status code failed"
    assert json.loads(response.text)['token'] == expected_token, "Valid Login User - token failed"


def test_invalidLoginUser(expected_status_code=400, expected_error_message="Missing password"):
    response = UserEndPoints().loginUser(data=Auth().inValid())
    assert response.status_code == expected_status_code, "Valid Login User - status code failed"
    assert json.loads(response.text)['error'] == expected_error_message, "Invalid Login User - error message failed"
