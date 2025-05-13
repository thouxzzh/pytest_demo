# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Global driver reference
# driver = None

# def setup_function():
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://tutorialsninja.com/demo/index.php?route=product/search")

# def teardown_function():
#     global driver
#     driver.quit()

# def test_valid_product():
#     driver.find_element(By.NAME, "search").clear()
#     driver.find_element(By.NAME, "search").send_keys("HP LP3065")
#     driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
#     act = driver.find_element(By.XPATH, "//h1[text()='Search - HP LP3065']").text
#     assert act == "Search - HP LP3065"

# def test_empty_product():
#     driver.find_element(By.NAME, "search").clear()
#     driver.find_element(By.NAME, "search").send_keys("")
#     driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
#     act = driver.find_element(By.XPATH, "//h2[text()='Products meeting the search criteria']").text
#     assert act == "Products meeting the search criteria"

# def test_invalid_product():
#     driver.find_element(By.NAME, "search").clear()
#     driver.find_element(By.NAME, "search").send_keys("honda")
#     driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
#     act = driver.find_element(By.XPATH, "//p[contains(text(),'no product')]").text
#     assert act == "There is no product that matches the search criteria."





# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Setup and teardown fixture
# @pytest.fixture
# def set_up_and_tear_down():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.com/")
    
#     try:
#         yield driver
#     finally:
#         driver.quit()  # Ensure that the browser is closed even if the test fails

# # Parametrized test function
# @pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
# def test_google_search(set_up_and_tear_down, search_term):
#     driver = set_up_and_tear_down

#     # Wait for the search box to be visible
#     search_box = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
#     )

#     search_box.clear()
#     search_box.send_keys(search_term)
#     search_box.submit()

#     # Wait for results page to load
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "search"))
#     )

#     # Basic assertion to check the page title contains the search term
#     assert search_term.lower() in driver.title.lower()
#     time.sleep(2)
