import time
import pytest
from selenium.webdriver.common.by import By
from Utilities.excelReader import get_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_data = get_data("C:\\Python_Selenium\\pytest_folder\\Task\\Excel\\login.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_logout(self):
        driver = self.driver
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        
        for index, data in enumerate(login_data):
            username, password, expected = data
            

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name")))

            driver.find_element(By.ID, "user-name").clear()
            driver.find_element(By.ID, "password").clear()

            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login-button"))
            )
            driver.find_element(By.ID, "login-button").click()

            if expected == "valid":
                exp = "Products"
                act = driver.find_element(By.XPATH, "//div[@class='product_label']").text
                assert exp == act

                driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
                driver.find_element(By.XPATH, "(//a[@class='bm-item menu-item'])[3]").click()
                print("Successfully logged out")

           
            elif expected == "locked":
                exp = "Epic sadface: Sorry, this user has been locked out."
                act = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
                print(exp)
                print(act)
                assert exp == act

           



