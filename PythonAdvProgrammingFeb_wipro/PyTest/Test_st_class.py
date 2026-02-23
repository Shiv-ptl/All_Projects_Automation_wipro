#used inside the class
#it will run for every class definition once ,it will run starting and ending of the class
import pytest
class Testclass:

    #class level set up
    def setup_class(cls):
        print("API Authorization needed with username and passward")

    def teardown_class(cls):
        print("Authorization closed.")

    @pytest.mark.sanity
    def testcase1(self):
        print("Testcase1 is executed.")

    # testcases 2
    def testcase2(self):
        print("Testcase2 is executed.")

    # testcases 3
    @pytest.mark.regression
    def test_case3(self):
        print("Testcase3 is executed.")

class Testclass2:

    #method level setup
    @pytest.mark.regression
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