from apiautomation.testcases.conftestt import *
from apiautomation.testcases.conftest import UserEndPoints
from apiautomation.common.application import Routes
from apiautomation.utilities.library import File_Operations as FO


def test_verifyStatusCodeCreateNewUser(url=Routes.create_user, data=FO().getJsonData(), expected_status_code=201):
    actual_status_code = UserEndPoints().create_user(url, data).status_code
    print("Received Status Code: ", actual_status_code)
    assert actual_status_code == expected_status_code, "Status Code Failed"


def test_verifyContentReceived(url=Routes.create_user, data=FO().getJsonData(), expected_job="QAleader Updated"):
    actual_text_received = json.loads(UserEndPoints().create_user(url, data).text)
    print("Received Job: ", actual_text_received['job'])
    assert actual_text_received['job'].casefold() == expected_job.casefold(), "Job Match Failed"
