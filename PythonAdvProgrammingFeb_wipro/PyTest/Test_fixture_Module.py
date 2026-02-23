import  pytest
@pytest.mark.usefixtures("setupapi")
def test_one():
    print("Tescase1")

def test_two():
    print("TestCase2")