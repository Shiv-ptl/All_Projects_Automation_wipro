#pip install pytest-check
import sys
from email.policy import strict

import pytest
import pytest_check as check

from LabSessions.Day2_feb06.labSession_3 import result


#basic assertion
#hard assertions-this will stop th eexecution of the test cases/test suite
#soft assertion will continue to run if the assertion fails

#basic assertion
def test_add():
    result = 0+5
    assert result==5

#check true or false
def test_boolean():
    assert True
    assert not False

#none value
def test_none():
    value = None
    assert value is None

#list assertion
def test_list():
    fruits = ["apple","banana","orabge"]
    assert "banana" in fruits

#Dict assertion

def test_dic():
    creds = {"username":"admin","password":"admin123"}
    assert creds["password"] =="admin123"

#comparing lists
def test_comparelist():
    assert [1,2,3] ==[1,2,3]

#assertion with custom message
def test_custommsg():
    result = 10
    assert result==10, "Result should be 5"

#soft assertion
def test_multiple():
    print("asdfg")
    check.equal(2,2)
    print("asdfg")
    check.equal(2,3)
    print("asdfg")
    check.equal(5,5)
    print("asdfg")

#xfail with condition
@pytest.mark.xfail(sys.platform == "win32",reason = "Bug on windows")
def test():
    print("test on windows")

    #this xfail will fail only on windows

#strict=True XFAIL FAILS THE TEST SUITE
pytest.mark.xfail(strict=True,reason = "Bug #123 is not fixed yet!!!")
def test_fun():
    assert True

