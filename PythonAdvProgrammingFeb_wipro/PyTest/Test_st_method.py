# used inside the class
# it will run for every class definition ,it will run starting and ending of the methods inside the class
# in case of inheritance setup and teardown are considered
import pytest

class Testclass2:

    #method level setup
    def setup_method(method):
        print("opening the browser..")

    def teardown_method(method):
        print("Closing the browser...")

    def testcase4(self):
        print("Testcase4 is executed.")

    # testcases 2
    def testcase5(self):
        print("Testcase5 is executed.")

    # testcases 3
    def test_case6(self):
        print("Testcase6 is executed.")

class Testclass3(Testclass2):
    def testcase1(self):
        print("Testcase1 is executed.")

    # testcases 2
    def testcase2(self):
        print("Testcase2 is executed.")