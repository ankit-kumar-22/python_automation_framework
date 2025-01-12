import pytest
from pages.login_page import LoginPage
from hamcrest import  assert_that

@pytest.mark.ui
def test_valid_login(driver, config, custom_logger):
    custom_logger.info("Navigating to the login page.")
    driver.get(f"{config['base_url']}")
    login_page = LoginPage(driver)
    login_page.login(config['username'], config['password'])
    assert_that("OrangeHRM", driver.title)

