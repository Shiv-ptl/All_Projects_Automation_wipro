import pytest

#module level -- runs once per module(file)
# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection

# setup_module - -> only one per file
# setup_class() → one per class
# setup_method() → one per class
# setup_function() → one per class


def setup_module(module):
    print("Open DataBase Connection...")

def teardown_module(module):
    print("Closing DataBase Connection...")

#testcases 1
def test_read():
    print("Reading the DB")

#testcases 2
def test_write():
    print("Writing the data in the DB.")

#testcases 3
def test_updating():
    print("Updating the DB.")
