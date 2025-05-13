import pytest
from selenium import webdriver
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("Browser", "b")
    driver = None

    if browser == "Chrome":
        driver = webdriver.Chrome()
    

    elif browser == "FireFox":
        driver = webdriver.Firefox()
    elif browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(5)

    app_url = read_config.get_config("link", "url")
    print(f"Opening URL: {app_url}")
    driver.get(app_url)

    request.cls.driver = driver
    yield
    driver.quit()
