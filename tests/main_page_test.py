import pytest
import allure
import requests
from tests.constants import Tokens, Urls


@allure.epic("Test Main Page smoke_test")
@pytest.mark.smoke_test
class TestMainPageSmoke:

    @pytest.mark.parametrize('url', Urls.LIST_URLS_PROD)
    def test_urls_prod(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        headers = Tokens.TOKEN_PROD
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == 200, f'{url} недоступен'

    @pytest.mark.parametrize('url', Urls.LIST_URLS_PROD)
    def test_open_prod(self, auth_user_admin_to_prod, driver, url):
        allure.dynamic.title(f'Проверить отсутствие ошибок при открытии {url} на сервере prod')
        driver.get(url)
        assert auth_user_admin_to_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_prod.check_error_notifications()]}'
