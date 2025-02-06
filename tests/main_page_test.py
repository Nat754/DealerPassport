import pytest
import allure
import requests
from selenium.common import TimeoutException
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

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.SELECT_DEALER_TEXT}')
    def test_button_select_dealer(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_select_dealer().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.SELECT_DEALER_TEXT, f'ОР: {HeaderConstant.SELECT_DEALER_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.PKD_TEXT}')
    def test_button_button_pkd(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_pkd().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.PKD_TEXT, f'ОР: {HeaderConstant.PKD_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.INTERRUPTION_TEXT}')
    def test_button_button_interruption(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_interruption().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.INTERRUPTION_TEXT, f'ОР: {HeaderConstant.INTERRUPTION_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.NOTICES_TEXT}')
    def test_button_button_notices(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_notices().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.NOTICES_TEXT, f'ОР: {HeaderConstant.NOTICES_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.DOCUMENTS_TEXT}')
    def test_button_button_documents(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_documents().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.DOCUMENTS_TEXT, f'ОР: {HeaderConstant.DOCUMENTS_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.ACCOUNTING_TEXT}')
    def test_button_button_accounting(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_accounting().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.ACCOUNTING_TEXT, f'ОР: {HeaderConstant.ACCOUNTING_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.SRR_TEXT}')
    def test_button_button_srr(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_srr().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.SRR_TEXT, f'ОР: {HeaderConstant.SRR_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение и кликабельность кнопки {HeaderConstant.REPORTS_TEXT}')
    def test_button_button_reports(self, auth_user_admin):
        try:
            text = auth_user_admin.check_button_reports().text
        except TimeoutException:
            text = ''
        assert text == HeaderConstant.REPORTS_TEXT, f'ОР: {HeaderConstant.REPORTS_TEXT}, ФР: {text}'

    @allure.title(f'Проверить отображение кнопок меню')
    def test_button_menu(self, auth_user_admin):
        text = [item.text for item in auth_user_admin.check_menu()]
        assert text == HeaderConstant.MENU_TEXT, f'ОР: {HeaderConstant.MENU_TEXT}, ФР: {text}'
