import pytest
import os
from dotenv import load_dotenv
from pages.main_page import MainPage
from tests.constants import Urls

load_dotenv()


# for dev
# @pytest.fixture
# def auth_user_admin(driver):
#     main_page = MainPage(driver)
#     url = Urls.MAIN_URL + Urls.AUTH
#     cookies = {'name': 'token', 'value': os.environ["SEO_ADMIN"]}
#     driver.get(url)
#     driver.add_cookie(cookies)
#     driver.get(Urls.MAIN_URL)
#     main_page.check_button_agree().click()
#     return main_page


# for test
# @pytest.fixture
# def auth_user_admin(driver):
#     main_page = MainPage(driver)
#     url = Urls.MAIN_URL + Urls.AUTH
#     cookies = {'name': 'token', 'value': os.environ["TEST_ADMIN"]}
#     driver.get(url)
#     driver.add_cookie(cookies)
#     driver.get(Urls.MAIN_URL)
#     main_page.check_button_agree().click()
#     return main_page
#
#
# for prod
@pytest.fixture
def auth_user_admin(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL + Urls.AUTH
    cookies = {'name': 'token', 'value': os.environ["PROD_ADMIN"]}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL)
    main_page.check_button_agree().click()
    return main_page
