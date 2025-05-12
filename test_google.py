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

# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('browser_ip',[('Chrome'),('FireFox')])
# @pytest.mark.parametrize('url_ip',['https://www.flipkart.com/','https://www.amazon.in/'])

# def test_browser(browser_ip,url_ip):
#     if browser_ip=="Chrome":
#        driver=webdriver.Chrome()
#     elif browser_ip=="FireFox":
#        driver=webdriver.Firefox()
#     driver.maximize_window()
#     driver.get(url_ip)
#     print(driver.title)
#     time.sleep(3)
#     driver.close()


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def set_up_and_tear_down():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_valid_product(set_up_and_tear_down):
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("HP LP3065")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act = driver.find_element(By.XPATH, "//h1[text()='Search - HP LP3065']").text
    exp = "Search - HP LP3065"
    assert act == exp

def test_empty_product(set_up_and_tear_down):
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act = driver.find_element(By.XPATH, "//h2[text()='Products meeting the search criteria']").text
    exp = "Products meeting the search criteria"
    assert act == exp

def test_invalid_product(set_up_and_tear_down):
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("honda")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act=driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    exp="There is no product that matches the search criteria."
    assert act==exp




    







