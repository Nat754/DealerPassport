import pytest
from pages.main_page import MainPage
from tests.constants import Urls, Tokens


@pytest.fixture
def auth_user_admin(driver):
    main_page = MainPage(driver)
    url = Urls.MAIN_URL + Urls.AUTH
    cookies = {'name': 'token', 'value': Tokens.TOKEN}
    driver.get(url)
    driver.add_cookie(cookies)
    driver.get(Urls.MAIN_URL)
    main_page.check_button_agree().click()
    return main_page
