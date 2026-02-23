#grouping - set of testcases run together - issue fox in that module
#give the name of group
import pytest


#testcases 1
def testcase1():
    print("Testcase1 is executed.")

#testcases 2
@pytest.mark.sanity
def testcase2():
    print("Testcase2 is executed.")

#testcases 3
@pytest.mark.regression
def test_case3():
    print("Testcase3 is executed.")

#testcases 4
@pytest.mark.db
def test_openbrowser():
    print("opening the browser")