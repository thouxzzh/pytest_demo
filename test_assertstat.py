import time
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

class TestParabank(softest.TestCase):
    def test_registration_and_login(self):
        driver = webdriver.Chrome()
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element(By.LINK_TEXT, "Register").click()

        fname = driver.find_element(By.ID, "customer.firstName")
        fname.send_keys("Thoushika")

        lname = driver.find_element(locate_with(By.TAG_NAME, "input").below(fname))
        lname.send_keys("Mary")

        address = driver.find_element(locate_with(By.TAG_NAME, "input").below(lname))
        address.send_keys("test123")

        city = driver.find_element(locate_with(By.TAG_NAME, "input").below(address))
        city.send_keys("Salem")

        state = driver.find_element(locate_with(By.TAG_NAME, "input").below(city))
        state.send_keys("Tamil Nadu")

        zip_code = driver.find_element(locate_with(By.TAG_NAME, "input").below(state))
        zip_code.send_keys("636007")

        phone = driver.find_element(locate_with(By.TAG_NAME, "input").below(zip_code))
        phone.send_keys("9876543210")

        ssn = driver.find_element(locate_with(By.TAG_NAME, "input").below(phone))
        ssn.send_keys("123456789")

        username = driver.find_element(locate_with(By.TAG_NAME, "input").below(ssn))
        username.send_keys("thanu")

        password = driver.find_element(locate_with(By.TAG_NAME, "input").below(username))
        password.send_keys("pass123")

        confirm_password = driver.find_element(By.XPATH, "//input[@id='customer.password']/following::input[1]")
        confirm_password.send_keys("pass123")

        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        time.sleep(3)
        self.soft_assert(self.assertIn, "Your account was created successfully", driver.page_source, "Registration failed")

        driver.find_element(By.LINK_TEXT, "Log Out").click()

        username = driver.find_element(By.XPATH, "(//input[@class='input'])[1]")
        password = driver.find_element(locate_with(By.XPATH, "(//input[@class='input'])[2]").below(username))
        username.send_keys("thanu")
        password.send_keys("pass123")

        driver.find_element(By.XPATH, "//input[@value='Log In']").click()

        time.sleep(3)
        self.soft_assert(self.assertIn, "Accounts Overview", driver.page_source, "Login failed")

        self.assert_all()
        driver.quit()
