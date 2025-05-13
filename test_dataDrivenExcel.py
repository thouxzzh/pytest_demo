# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Utilities import excelReader

# @pytest.mark.parametrize("username,password",excelReader.get_data("ExcelFiles/loginData.xlsx","login"))
# class TestLogin1:
#     def test_validlogin1(self,username,password):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://www.demoblaze.com/index.html")
#         self.driver.find_element(By.ID,value="login2").click()
#         time.sleep(5)
#         self.driver.find_element(By.ID,"loginusername").send_keys(username)
#         time.sleep(5)
#         self.driver.find_element(By.Id,"loginpassword").send_keys(password)
#         self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
#         time.sleep(5)
#         assert self.driver.find_element(By.ID,"logout2").is_displayed()



import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader

@pytest.mark.parametrize("username,password", excelReader.get_data("C:\Python_Selenium\pytest_folder\ExcelFiles\loginData.xlsx.xlsx", "Sheet1"))
class TestLogin1:
    def test_validlogin1(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(5)
        if password=="123":
           alert1=self.driver.switch_to.alert
           exp="Wrong password."
           act=alert1.text
           print(act)
           assert exp==act
           alert1.accept()
        else:
           assert self.driver.find_element(By.ID, "logout2").is_displayed()
        self.driver.close()
         
