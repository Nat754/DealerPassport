import allure
import pytest
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions


@allure.epic('ExternalApiTests')
@pytest.mark.manual_run
class ExternalApi:
    url = Urls
    token = Tokens
    page = RESTApi()
    header = Headers
    const = IntegrationsConstants
    code = StatusCodes


@allure.suite('ExternalApi')
@pytest.mark.manual_run
class TestExternalApi(ExternalApi):

    @allure.title('Получить список существующих позиций')
    def test_get_employees_positions(self):
        url = (f'{self.url.MAIN_URL}/external-api/employees/positions?actualOn=2026-02-20&statuses[]=active&ids['
               f']=1197057857')
        headers = self.header.HEADERS_EXPORT_NEW
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить список сотрудников')
    def test_get_employees(self):
        url = f'{self.url.MAIN_URL}/external-api/employees?actualOn=2026-02-20&statuses[]=verified'
        headers = self.header.HEADERS_EXPORT_NEW
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить список дилеров')
    def test_get_dealers(self):
        url = f'{self.url.MAIN_URL}/external-api/dealers?updateAt=2026-03-15'
        headers = self.header.HEADERS_EXPORT_NEW
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить список сотрудников')
    def test_get_dealers_id_personal(self):
        url = f'{self.url.MAIN_URL}/external-api/dealers/1197057857/personal'
        headers = self.header.HEADERS_EXPORT_NEW
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)
