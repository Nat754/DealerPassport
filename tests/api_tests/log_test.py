import allure
import pytest
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions


@allure.epic('LogsTest')
class TestApi:
    url = Urls
    token = Tokens
    page = RESTApi()
    header = Headers
    const = IntegrationsConstants
    code = StatusCodes


@allure.suite('Logs')
@pytest.mark.manual_run
class TestLog(TestApi):

    @allure.title('Получить логи активности пользователей')
    def test_get_logs_activity(self):
        url = f'{self.url.MAIN_URL}/internal-api/logs/activity'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить список всех типов событий')
    def test_get_logs_event_types(self):
        url = f'{self.url.MAIN_URL}/internal-api/logs/event-types'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('генерировать Excel отчёт по логам активности')
    def test_get_logs_activity_report(self):
        url = f'{self.url.MAIN_URL}/internal-api/logs/activity-report'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить логи cron задач')
    def test_get_logs_cron(self):
        url = f'{self.url.MAIN_URL}/internal-api/logs/cron?name=LadaAcademiaIntegration'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить список уникальных имен cron задач')
    def test_get_logs_cron_names(self):
        url = f'{self.url.MAIN_URL}/internal-api/logs/cron/names'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)
