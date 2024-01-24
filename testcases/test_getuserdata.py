# URL = Routes().get_single_user.format(id=2)
import json


# @pytest.mark.usefixtures(get_user)
def test_verifyStatusCodeGetUser(get_user):
    actual_status_code = get_user.status_code
    assert actual_status_code == 200


def test_verifyContentGetUser(get_user, expected_email="janet.weaver@reqres.in"):
    actual_text = json.loads(get_user.text)
    assert actual_text['data']['email'] == expected_email, "Get User Content - verification"
