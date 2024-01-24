import requests

from common.application import Routes
from utilities.library import File_Operations

login_data = File_Operations().getJsonData(open("/usr/local/google/home/sateeshg/apiautomation/loginuser", "r"))


class Auth:
    def valid(self):
        valid_data = login_data['valid'][0]
        return valid_data

    def inValid(self):
        return login_data['invalid'][0]
