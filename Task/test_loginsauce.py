import pytest
from selenium.webdriver.common.by import By
from Utilities.excelReader import get_data


login_data = get_data("C:\Python_Selenium\pytest_folder\Task\Excel\login.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.mark.parametrize("username,password,expected", login_data)
    def test_login_logout(self, username, password,expected):
        driver = self.driver

        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        if expected=="valid":
            exp="Products"
            act=driver.find_element(By.XPATH,"//div[@class='product_label']").text
            assert exp==act
            button=driver.find_element(By.XPATH,"//button[text()='Open Menu']").click()
            log_out=driver.find_element(By.XPATH,"(//a[@class='bm-item menu-item'])[3]").click()
            print("Successfully logged out")

        elif expected=="locked":
            exp="Epic sadface: Sorry, this user has been locked out."
            act=driver.find_element(By.XPATH,"//h3[@data-test='error']").text
            print(exp)
            print(act)
            assert exp==act
        driver.quit()





        

