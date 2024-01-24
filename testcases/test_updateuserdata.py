import json

from apiautomation.testcases.conftest import UserEndPoints
from apiautomation.common.application import Routes
from apiautomation.utilities.library import File_Operations

# url = Routes().update_user
# data = File_Operations().getJsonData(open("/usr/local/google/home/sateeshg/createuser", "r"))


def test_verifyStatusCodeUpdateUser(update_user, expected_status_code=200):
    # response = UserEndPoints().update_user()
    print("Update User - Actual Status Code:", update_user.status_code)
    assert update_user.status_code == expected_status_code


def test_verifyUpdateUserFields(update_user, expected_email="emmalis.wonglee@reqres.in", expected_first_name="Emmalis", expected_last_name="Wonglee"):
    # response = UserEndPoints().update_user()
    print("Actual Data: ", json.loads(update_user.text))
    assert json.loads(update_user.text)['email'] == expected_email
    assert json.loads(update_user.text)['first_name'].casefold() == expected_first_name.casefold()
    assert json.loads(update_user.text)['last_name'].casefold() == expected_last_name.casefold()
