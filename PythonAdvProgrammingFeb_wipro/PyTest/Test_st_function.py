#


import pytest


def setup_function(function):
    print("opening the browser..")

def teardown_function(function):
    print("Closing the browser...")
#testcases 1
def testcase1():
    print("Testcase1 is executed.")

#testcases 2
def testcase2():
    print("Testcase2 is executed.")

#testcases 3
def test_case3():
    print("Testcase3 is executed.")