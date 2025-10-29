from pprint import pprint
import allure
import pytest
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, IntegrationsConstants, Tokens, StatusCodes, Assertions


@allure.epic("Test integrations")
@pytest.mark.auto_test
class TestIntegrations:
    const = IntegrationsConstants
    url = Urls
    token = Tokens
    page = RESTApi
    status = StatusCodes
    assertion = Assertions

    @allure.title('Проверка доступности MSPortal Test')
    def test_get_ms_portal_test(self):
        response_test = self.page.get(self.const.url_test, headers=self.token.MS_PROD)
        assert response_test.status_code == self.status.OK, f'{self.assertion.STATUS} - {response_test.text}'

    @allure.title('Проверка доступности MSPortal Prod')
    def test_get_ms_portal_prod(self):
        response_prod = self.page.get(self.const.url_test, headers=self.token.MS_PROD)
        assert response_prod.status_code == self.status.OK, f'{self.assertion.STATUS} - {response_prod.text}'

    @allure.title('Получение данные качества тест MSPortal')
    def test_get_indicators_test(self):
        response_test = self.page.get(self.const.url_test, headers=self.token.MS_PROD)
        # dealers = [item['dealer_id'] for item in response_test.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на тесте ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [item['mark'] for item in response_test if item['dealer_id'] == dealer], sep='\n')
        assert response_test.status_code == self.status.OK, f'{self.assertion.STATUS} - {response_test.text}'

    @allure.title('Получить данные качества прод MSPortal')
    def test_get_indicators_prod(self):
        response_prod = self.page.get(url=self.const.url_prod, headers=self.token.MS_PROD)
        # dealers = [item['dealer_id'] for item in response_prod.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на прод ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [item['mark'] for item in response_prod if item['dealer_id'] == dealer], sep='\n')
        assert response_prod.status_code == self.status.OK, f'{self.assertion.STATUS} - {response_prod.text}'

    @allure.title('Проверить доступности Candidates')
    def test_get_candidates_health(self):
        url = f'{self.url.CANDIDATES_URL}/health'
        response = self.page.get(url)
        # pprint(response.json())
        assert response.status_code == self.status.OK, f'{self.assertion.STATUS}'

    @allure.title('Получить ДЦ из Реестра')
    def test_get_registry_dealers(self):
        url = f'{self.url.REGISTRY_URL}/AVWS_PPD_REESTR_DLR'
        headers = self.token.REGISTRY
        response = self.page.get(url, headers=headers)
        # pprint(response.json())
        # print([(item['DEALER_ID'], item['PN_INFO']) for item in response.json() if item['DEALER_ID'] == 6427884196])
        print()
        print('DEALER_ID', 'DEALER_NAME', "DEALER_INN", "DEALER_FILIALCODE", 'UR_DIST_CODE')
        pprint([(item['DEALER_ID'], item['DEALER_NAME'], item["DEALER_INN"], item["DEALER_FILIALCODE"],
                 item['UR_DIST_CODE']) for item in response.json() if type(item['UR_DIST_CODE']) != type(10)])
        assert response.status_code == self.status.OK, f'{self.assertion.STATUS} - {response.text}'

    @allure.title('Получить пользователей из Реестра')
    def test_get_registry_users(self):
        url = f'{self.url.REGISTRY_URL}/AVWS_PPD_USER_REESTR'
        headers = self.token.REGISTRY
        response = self.page.get(url, headers=headers)
        assert response.status_code == self.status.OK, f'{self.assertion.STATUS} - {response.text}'
