import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_valid_product(set_up_and_tear_down):
    driver = set_up_and_tear_down
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("HP LP3065")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act = driver.find_element(By.XPATH, "//h1[text()='Search - HP LP3065']").text
    exp = "Search - HP LP3065"
    assert act == exp

def test_empty_product(set_up_and_tear_down):
    driver = set_up_and_tear_down
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act = driver.find_element(By.XPATH, "//h2[text()='Products meeting the search criteria']").text
    exp = "Products meeting the search criteria"
    assert act == exp

def test_invalid_product(set_up_and_tear_down):
    driver = set_up_and_tear_down
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("honda")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    act=driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    exp="There is no product that matches the search criteria."
    assert act==exp




    







