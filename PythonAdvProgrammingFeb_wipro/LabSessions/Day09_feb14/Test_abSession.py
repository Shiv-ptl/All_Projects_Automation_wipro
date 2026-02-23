# You have 5 parameterized cases. 2 are known bugs. Mark only those 2 cases as xfail without marking entire test.

import pytest

@pytest.mark.parametrize(
    "username,password",
    [
        ("valid_user", "valid_pass"),
        ("admin", "admin123"),
        pytest.param("locked_user", "pass123", marks=pytest.mark.xfail(reason="Account lock bug")),
        pytest.param("guest", "guest123", marks=pytest.mark.xfail(reason="Guest login bug")),
        ("new_user", "newpass")
    ]
)
def test_login(username, password):
    assert len(password) >= 6




# 1Write a test that is skipped because a feature is not implemented yet.

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment_feature():
    assert True

# 2.write a test that runs only on Linux and skips on Windows.
import sys

@pytest.mark.skipif(sys.platform.startswith("win"), reason="Runs only on Linux")
def test_linux_only():
    assert True

# 3.Write a test that checks an API health endpoint. If status code is not 200 → skip the test dynamically.
import requests

def test_api_health():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code != 200:
        pytest.skip("API not healthy, skipping test")

    assert response.status_code == 200

# 4.Mark a failing test as xfail with reason: "Bug #123"

@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 1 == 2