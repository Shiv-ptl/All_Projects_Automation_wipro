import pytest

from Pages.Login import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    # def test_title(self):
    #     print(self.driver.title)
    #     assert "OrangeHRM" in self.driver.title

    def test_valid_login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        lp = LoginPage(self.driver)
        lp.login("Admin","admin123")
        assert "Dashboard" in driver.title




    #def test_invalid_login(self):

