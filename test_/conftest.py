import pytest
from Library.config import Configuration
from selenium import webdriver


@pytest.fixture(params=["Chrome","firefox","Edge"])
def init_driver(request):
    global driver
    browser = request.param
    print(browser)
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=Configuration.FIREFOX_PATH)

    else:
        driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

    driver.get(Configuration.URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    path = r'C:\Users\LENOVO\PycharmProjects\BMS_Events\screenshot\\'
    driver.save_screenshot(path+"test_events.png")
    driver.close()
