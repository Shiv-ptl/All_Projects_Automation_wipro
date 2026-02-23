#skip - if defects are there
#skip - if the testcases are absolute
#windows ,mobile - os dependency
# browsers
#   @pytest.mark.skip


import pytest


#testcases 1
def testcase1():
    print("Testcase1 is executed.")

#testcases 2
@pytest.mark.skip
def testcase2():
    print("Testcase2 is executed.")

#testcases 3
def test_case3():
    print("Testcase3 is executed.")

#testcases 4
def test_openbrowser():
    print("opening the browser")