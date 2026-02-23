#fixtures are the peice of code which are run before the testcases or after the tests

import pytest

@pytest.fixture
def simple_data():
    return 45

def testCase1(simple_data):
    assert simple_data==45

@pytest.fixture()
def api_url():
    return "https//api.example.com"

def test_api(api_url):
    assert "https" in api_url


#in Test_Discovery.py we used this fixture to show it can be used in other files also