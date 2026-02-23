# unit testing is type of testing done by the developers
# what component they have developed they do the testing for it before integrating it to the other modules
# get defects earlier
# Pytest in python , junit and nunit - java
# pytest is used ny developers and testers


#test discovery -- rules used to create the pytest tests

#fun should start with test_

import pytest




#testcases 1
def testcase1():
    print("Testcase1 is executed.")

#testcases 2
def testcase2():
    print("Testcase2 is executed.")

#testcases 3
def test_case3():
    print("Testcase3 is executed.")

#testcases 4
def testopenbrowser():
    print("opening the browser")


#pytest .\Test_Discovery.py  to run the Test_Discovery.py file in terminal

#to generate the report  -->pip install pytest-html
#pytest .\Test_Discovery.py -v -s --html=Test_Discovery_report.html


#fixture use from other file
from Test_SimpleFixture import api_url
def test_api(api_url):
    assert "https" in api_url