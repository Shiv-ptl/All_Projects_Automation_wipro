#parameterization ---- testing multiple set of test data with the same function
# @pytest.mark.parametrize()


#no parameter used

def test_add1():
    assert 2+3 ==5

def test_add2():
    assert 4+5==9


import pytest
#multiple parameters
@pytest.mark.parametrize("a,b,result",[
    (2,3,5),
    (4,5,9),
    (10,2,12)

])

def test_add(a,b,result):
    assert a+b ==result

@pytest.mark.parametrize("number",[12,89,8,4,88])
#single parameter
def test_even(number):
    assert number%2==0


#dictionary items
@pytest.mark.parametrize("payload",[
    {"name": "Shivanshu Patel","age":22},
    {"name":"Vinayak Patel","age": 16}
])

def test_create_user(payload):
    assert payload["age"]>18