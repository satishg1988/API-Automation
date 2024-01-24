import requests

from common.application import Routes
from utilities.library import File_Operations

create_data = File_Operations().getJsonData(open("/usr/local/google/home/sateeshg/apiautomation/createuser", "r"))
update_data = File_Operations().getJsonData(open("/usr/local/google/home/sateeshg/apiautomation/updateuser", "r"))
# login_data = File_Operations().getJsonData(open("/usr/local/google/home/sateeshg/apiautomation/loginuser", "r"))


class UserEndPoints:
    def createUser(self, url):
        response = requests.post(url, data=create_data)
        print("Create User: ", response)
        # print("Text Is: ", response_received.text)
        return response

    def getUser(self):
        response = requests.get(url=Routes.get_single_user.format(id=2))
        print("Get User: ", response)
        return response

    def updateUser(self):
        response = requests.put(url=Routes.update_user.format(id=2), data=update_data)
        print("Update User: ", response.text)
        return response

    def loginUser(self, data):
        response = requests.post(url=Routes.login_user, json=data)
        print("Login User: ", response)
        return response


# uep = UserEndPoints()
# # uep.create_user(url=Routes.create_user)
# uep.loginUser()
# uep.update_user(url=Routes.update_user, data=FO().getJsonData(open("/usr/local/google/home/sateeshg/createuser", "r")))
