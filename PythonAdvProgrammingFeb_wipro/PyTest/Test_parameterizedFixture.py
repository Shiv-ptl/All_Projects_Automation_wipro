import pytest

#request - pytest object that contains informaiton about
#who is calling the fixture and with what data


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser: ",request.param)
    return request.param

def test_browser(browser):
    assert browser in ["chrome","firefox"]


@pytest.fixture(params=[2,4,6,12])
def iseven(request):
    return request.param

def test_even(iseven):
    assert iseven %2==0


#dictionary items
@pytest.fixture(params=[
    {"name": "Shivanshu Patel","age":22},
    {"name":"Vinayak Patel","age": 19}
])
def user(request):
    return request.param

def test_create_user(user):
    assert user["age"]>18