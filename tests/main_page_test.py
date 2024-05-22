import time
import pytest
import allure
import requests
from tests.constants import Tokens, Urls


@allure.epic("Test Main Page smoke_test")
@pytest.mark.smoke_test
class TestMainPageSmoke:

    @pytest.mark.parametrize('url', Urls.LIST_URLS_SEO + Urls.LIST_URLS_SEO_PROD)
    def test_urls_seo(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        headers = Tokens.TOKEN_SEO
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200, f'{url} недоступен'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_PROD)
    def test_urls_prod(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        headers = Tokens.TOKEN_PROD
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200, f'{url} недоступен'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_SEO)
    def test_open_seo(self, auth_user_admin_to_seo, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url} на сервере СЕО')
        driver.get(url)
        assert auth_user_admin_to_seo.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_seo.check_error_notifications()]}'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_SEO_PROD)
    def test_open_seo_prod(self, auth_user_admin_to_seo_prod, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url} на сервере СЕО prod')
        driver.get(url)
        assert auth_user_admin_to_seo_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_seo_prod.check_error_notifications()]}'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_PROD)
    def test_open_prod(self, auth_user_admin_to_prod, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url} на сервере prod')
        driver.get(url)
        assert auth_user_admin_to_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_prod.check_error_notifications()]}'


@allure.epic("Test Main Page regression_test")
@pytest.mark.regression_test
class TestMainPageRegression:

    @allure.title('Проверка корректности перехода по ссылке Редактор СЕО')
    def test_clickable_and_redirect_button_editor(self, auth_user_admin_to_seo_prod, driver):
        time.sleep(2)
        auth_user_admin_to_seo_prod.check_button_editor().click()
        assert driver.current_url == Urls.MAIN_URL_SEO_PROD + Urls.EDITOR_URL, 'Не произошел переход на страницу Редактор'

    @allure.title('Проверка корректности перехода по ссылке Отчеты СЕО')
    def test_clickable_and_redirect_button_reports(self, auth_user_admin_to_seo_prod, driver):
        time.sleep(2)
        auth_user_admin_to_seo_prod.check_button_reports().click()
        time.sleep(3)
        assert driver.current_url == Urls.MAIN_URL_SEO_PROD + Urls.REPORTS_URL, \
            'Не произошел переход на страницу Отчеты'


@pytest.mark.skip
@allure.epic("Test Main Page TEST")
@pytest.mark.vpn_test
class TestMainPageTEST:

    @pytest.mark.parametrize('url', Urls.LIST_URLS_TEST)
    def test_urls_vpn(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        headers = Tokens.TOKEN_TEST
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200, f'{url} недоступен'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_TEST)
    def test_open_vpn(self, auth_user_admin_to_test, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url} на сервере TEST VAZ')
        driver.get(url)
        assert auth_user_admin_to_test.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_test.check_error_notifications()]}'
