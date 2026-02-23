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

#testcases 5
def test_case5():
    print("Testcase5 is executed.")

def test_login():
    print("Login test is executed.")

# pytest .\Test_parallel.py -n -3
#pytest .\Test_parallel.py -n -3 --html=report.html

#
# single testcase - pytest -k "test_login" -n 5 --html=report.html
# pytest .\Test_Parallel.py -n -3 --html=report.html