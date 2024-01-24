import pytest
from common.endpoints import UserEndPoints
from common.application import Routes


@pytest.fixture
def get_user():
    response = UserEndPoints().getUser()
    return response


@pytest.fixture
def update_user():
    response = UserEndPoints().updateUser()
    return response
