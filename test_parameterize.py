import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('browser_ip',[('Chrome'),('FireFox')])
@pytest.mark.parametrize('url_ip',['https://www.flipkart.com/','https://www.amazon.in/'])

def test_browser(browser_ip,url_ip):
    if browser_ip=="Chrome":
       driver=webdriver.Chrome()
    elif browser_ip=="FireFox":
       driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(url_ip)
    print(driver.title)
    time.sleep(3)
    driver.close()