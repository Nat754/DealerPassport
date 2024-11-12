import pytest
import allure
import requests
from tests.constants import Tokens, Urls, HeaderConstant


@allure.epic("Тестирование главной страницы")
@pytest.mark.smoke_test
class TestMainPageSmoke:

    @pytest.mark.parametrize('url', Urls.LIST_URLS)
    def test_get_urls(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        headers = Tokens.TOKEN_PROD
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200, f'{url} недоступен'

    @pytest.mark.parametrize('url', Urls.LIST_URLS)
    def test_open_url(self, auth_user_admin, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url}')
        driver.get(url)
        assert auth_user_admin.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin.check_error_notifications()]}'

    @allure.title(f'Проверить поиск по кнопке {HeaderConstant.SELECT_DEALER_TEXT}')
    def test_find_dealer(self, auth_user_admin):
        text = auth_user_admin.check_button_select_dealer().text
        assert text == HeaderConstant.SELECT_DEALER_TEXT, f'ОР: {HeaderConstant.SELECT_DEALER_TEXT}, ФР: {text}'
        auth_user_admin.check_button_select_dealer().click()
        auth_user_admin.check_select_find_dealer(HeaderConstant.DEALER_NAME)
        dealers = auth_user_admin.check_select_dealers()
        assert {HeaderConstant.DEALER_NAME in _ for _ in dealers} == {True}, \
            f'{HeaderConstant.DEALER_NAME} не найден в {dealers}'
