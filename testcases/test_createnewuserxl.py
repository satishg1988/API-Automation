import json
from apiautomation.common.application import Routes

from apiautomation.utilities.library import File_Operations
from apiautomation.testcases.conftest import UserEndPoints

createuser_url = Routes.create_user


def test_createnewuserexcl(url=createuser_url, expected_statuscode=201):
    fo = File_Operations()
    rw_count = fo.getRowCount()
    keynames_li = fo.getKeyNamesList()
    users_jsondata = fo.getJsonData()
    print("Users Data from file in json format: ", users_jsondata['name'])

    for r in range(2, rw_count + 1):
        updated_users_jsondata = fo.updateRequestWithData(r, users_jsondata, keynames_li)
        print("Name and Job values assigned to json format name & job: ", updated_users_jsondata['name'], updated_users_jsondata['job'])
        response = UserEndPoints().create_user(url, updated_users_jsondata)
        print("Actual Status Code Received: ", response.status_code)
        text_post_request = json.loads(response.text)
        print("Text Received From Post Request Response: ", text_post_request)
        print("------------------------------------------------------------------")
        assert response.status_code == expected_statuscode, "Status Code Not Matched"
        print("Actual Name Received: ", text_post_request['name'])
        if text_post_request['name'] == "testname":
            print("Actual Name Matched Expected Name")
            break
    return text_post_request['name'], text_post_request['job']


assert test_createnewuserexcl() == ("testname", "test role"), "Assert Failed"
