#scope is run before and after every function

import pytest

@pytest.mark.usefixtures("openbrowser")
def test_logic():
    print("Enter the name")
    print("Enter the password")
    print("click the login button.")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user logged out.")