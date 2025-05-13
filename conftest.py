# import pytest
# from selenium import webdriver

# @pytest.fixture()
# def set_up_and_tear_down():
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://tutorialsninja.com/demo/")
#     yield
#     driver.quit()



# conftest.py
# import pytest
# from selenium import webdriver

# @pytest.fixture()
# def set_up_and_tear_down():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.com")  # Go to Google home page
#     yield driver  # Yielding driver so it can be used in the test
#     driver.quit()



# import pytest
# from selenium import webdriver

# @pytest.fixture(params=["chrome","firefox","edge"])
# def set_up_and_tear_down(request):
#     if request.param=="chrome":
#         driver=webdriver.Chrome()
#     elif request.param=="firefox":
#         driver=webdriver.Firefox()
#     elif request.param=="edge":
#         driver=webdriver.Edge()


#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.com")  # Go to Google home page
#     yield driver # Yielding driver so it can be used in the test
#     driver.quit()


import pytest
from selenium import webdriver
import read_config
@pytest.fixture()
def setup_and_teardown(request):
    browser=read_config.get_config("basic info","browser")
    driver=None
    if browser=="Chrome":
       driver=webdriver.Chrome()
    elif browser=="FireFox":
       driver=webdriver.Firefox()
    elif browser=="Edge":
       driver=webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    app_url=read_config.get_config("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()