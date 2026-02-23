#xfail is a marker used to indicate that is expected to fail due to a known issue

import pytest

@pytest.mark.xfail(reason= "Known bug in the third-party library")
def test_function_with_bug():
    assert (1+1) ==1 #this assertion will fail as expected

#testcases 1
def testcase1():
    print("Testcase1 is executed.")

#testcases 2
def testcase2():
    print("Testcase2 is executed.")

#testcases 3
def test_case3():
    print("Testcase3 is executed.")