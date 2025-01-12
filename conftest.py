import pytest
from selenium import webdriver

from configs.configs import load_config_values
from utils.api_utils import APIUtils
from utils.custom_logger import get_logger



@pytest.fixture(scope="session")
def config():
    configs = load_config_values(module_name="module_a")
    return {
        "base_url": configs['urls']['BASE_URL'],
        "api_base_url":  configs['urls']['API_URL'],
        "browser": configs['browser']['browser_name'],
        "username": configs['accounts']['USERNAME'],
        "password": configs['accounts']['PASSWORD']
    }


@pytest.fixture(scope="function")
def driver(config):
    if config["browser"] == "chrome":
        driver = webdriver.Chrome()
    elif config["browser"] == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_utils():
    return APIUtils()


@pytest.fixture(scope="session")
def custom_logger():
    """
    Provides a logger instance for the test session.
    """
    return get_logger()