import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_term', ['selenium', 'pytest', 'selenium_locators'])
def test_google_search(search_term):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in/")
    driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys(search_term)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "gNO89b").click()
    time.sleep(2)
    driver.quit()