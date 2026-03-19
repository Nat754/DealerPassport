import allure
import pytest
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions


@allure.epic('ApiTestsPD')
@pytest.mark.manual_run
class TestApi:
    url = Urls
    token = Tokens
    page = RESTApi()
    header = Headers
    const = IntegrationsConstants
    code = StatusCodes

    @allure.title('Возвращает все поля, которые можно будет запросить у дилера')
    def test_get_dealers_export_fields(self):
        url = f'{self.url.MAIN_URL}/api/v1/dealers/export-fields'
        headers = self.header.HEADERS_EXPORT
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Возвращает всех дилеров Активных???')
    def test_get_dealers(self):
        url = f'{self.url.MAIN_URL}/api/v1/dealers?status[]=active'
        headers = self.header.HEADERS_EXPORT
        response = self.page.get(url, headers=headers)
        print(f"Всего получено {len(response.json()['dealers'])} ДЦ")
        Assertions.assert_status_code(response, self.code.OK)
