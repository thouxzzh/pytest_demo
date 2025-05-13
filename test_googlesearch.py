# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('search_term', ['selenium', 'pytest', 'selenium_locators'])
# def test_google_search(search_term):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.co.in/")
#     driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys(search_term)
#     time.sleep(2)
#     driver.find_element(By.CLASS_NAME, "gNO89b").click()
#     time.sleep(2)
#     driver.quit()





# test_google.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
def test_google_search(set_up_and_tear_down, search_term):
    driver = set_up_and_tear_down  # Use the driver from the fixture

    # Wait for the search box to be visible before interacting with it
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )

    search_box.send_keys(search_term)
    search_box.submit()  # Submit the search
    time.sleep(2)  # Wait for search results to load (you can also use WebDriverWait here)

