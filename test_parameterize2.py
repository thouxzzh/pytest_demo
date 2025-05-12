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




    







