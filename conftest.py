import datetime

import pytest
from selenium import webdriver
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser. Default option is chrome")
    parser.addoption("--headless", action="store_true", help="headless режим. только в False(по умолчанию) или True")
    parser.addoption("--url", help="URL")
# parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--remote", default=False)
    parser.addoption("--executor", default="localhost")
#   parser.addoption("--user", help="username for remote virtual machine")
    parser.addoption("--password", help="password for remote virtual machine")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")

    # log_level = request.config.getoption("--log_level")
    # logger = logging.getLogger(request.node.name)
    # file_handler = logging.FileHandler(f"tests/{request.node.name}.log")
    # file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    # logger.addHandler(file_handler)
    # logger.setLevel(level=log_level)


    if not remote:
        driver = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            driver = webdriver.Chrome(options=options)

        if browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless=new')
            options.add_argument('--enable-chrome-browser-cloud-management')
            driver = webdriver.Edge(options=options)

    # driver.log_level = log_level
    # driver.logger = logger
    # driver.test_name = request.node.name

    driver.maximize_window()
    driver.get(f"http://{executor}")
    yield driver
    driver.quit


@pytest.fixture
def base_url(request):
    executor = request.config.getoption("--executor")
    url = f"http://{executor}"
    return url


@pytest.fixture(scope="session")
def api_url():
    return "https://api.openbrewerydb.org/v1/breweries"