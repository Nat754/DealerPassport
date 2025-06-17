import allure
import pytest
from pages.rest_api_page import RESTApi
from tests.constants import Urls, IntegrationsConstants, Tokens


@allure.epic("Test integrations")
@pytest.mark.auto_test
class TestIntegrations:
    const = IntegrationsConstants
    url = Urls
    token = Tokens
    page = RESTApi()

    @allure.title('Проверка доступности MSPortal Test')
    def test_get_ms_portal_test(self):
        response_test = self.page.get(self.const.url_test, headers=self.token.MS_PROD)
        assert response_test.status_code == 200, 'Сервер MS Portal Test недоступен'

    @allure.title('Проверка доступности MSPortal Prod')
    def test_get_ms_portal_prod(self):
        response_prod = self.page.get(self.const.url_test, headers=self.token.MS_PROD)
        assert response_prod.status_code == 200, 'Сервер MS Portal Prod недоступен'

    @allure.title('Получение данных тест MSPortal')
    def test_get_indicators_test(self):
        response_test = self.page.get(self.const.url_test, headers=Tokens.MS_PROD)
        # dealers = [item['dealer_id'] for item in response_test.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на тесте ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [item['mark'] for item in response_test if item['dealer_id'] == dealer], sep='\n')
        assert response_test.status_code == 200, 'Сервер MS Portal Test недоступен'

    @allure.title('Получение данных прод MSPortal')
    def test_get_indicators_prod(self):
        response_prod = self.page.get(url=self.const.url_prod, headers=Tokens.MS_PROD)
        # dealers = [item['dealer_id'] for item in response_prod.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на прод ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [item['mark'] for item in response_prod if item['dealer_id'] == dealer], sep='\n')
        assert response_prod.status_code == 200, 'Сервер MS Portal Prod недоступен'

    @allure.title('Проверка доступности Candidates')
    def test_get_candidates_health(self):
        url = f'{self.url.CANDIDATES_URL}/health'
        response = self.page.get(url)
        assert response.status_code == 200, 'Сервер Отбора кандидатов недоступен'
