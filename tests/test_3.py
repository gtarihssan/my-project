"""import pytest

from django.contrib.auth.models import User

@pytest.fixture(scope="class")
def user_model(request):
    request.cls.num=1

# we use request and cls to deffinde the attribute of the test class as a class attribute 
# the decorator (@pytest.mark.usefixtures) used to implemet the fixture into the test class 
# with the decorator we should put the fixture name bettwen to brakset 


@pytest.mark.usefixtures("user_model")
class TestUsers:

    def test_user(self):
        assert self.num==1

"""