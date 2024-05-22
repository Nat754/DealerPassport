import pytest
import os
from dotenv import load_dotenv
from pages.main_page import MainPage
from tests.constants import Urls

load_dotenv()


@pytest.fixture
def auth_user_admin_to_seo(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL_SEO + Urls.AUTH
    cookies = {'name': 'token', 'value': os.environ["SEO_ADMIN"]}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL_SEO)
    main_page.check_button_agree().click()
    return main_page


@pytest.fixture
def auth_user_admin_to_seo_prod(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL_SEO_PROD + Urls.AUTH
    cookies = {'name': 'token', 'value': os.environ["SEO_ADMIN"]}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL_SEO_PROD)
    main_page.check_button_agree().click()
    return main_page


@pytest.fixture
def auth_user_admin_to_test(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL_TEST + Urls.AUTH
    cookies = {'name': 'token', 'value': os.environ["TEST_ADMIN"]}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL_TEST)
    main_page.check_button_agree().click()
    return main_page


@pytest.fixture
def auth_user_admin_to_prod(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL_PROD + Urls.AUTH
    cookies = {'name': 'token', 'value': os.environ["PROD_ADMIN"]}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL_PROD)
    main_page.check_button_agree().click()
    return main_page
