"""import pytest

from django.contrib.auth.models import User


# arrange
@pytest.fixture
def fixture_test(db):
    #act
    print('the fixture')
    User.objects.create_user('hssan')
    return User.objects.count()


def test_1(fixture_test):
    print('test1')
    assert fixture_test==1


def test_user(fixture_test):
    print('fixture traiting')
    #assert
    assert fixture_test==1
"""