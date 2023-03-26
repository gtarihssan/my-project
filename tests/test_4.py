import pytest 
import tempfile


@pytest.fixture
def usefix():
    return "hssan"


@pytest.fixture
def setup_teardown():
    print('setup')
    yield
    print('teardown')

@pytest.fixture
def fixture1():
    with tempfile.TemporaryDirectory() as tmdir:
        yield tmdir

def test_1(setup_teardown):
    print('test success')
    assert 1==1



@pytest.mark.usefixtures('fixture1')
def test_2():
    print(type(fixture1))
    assert 1==1
    

def test_3(fixture1):
    print(fixture1)
