import allure
import pytest
import requests
from pages.assertions import Assertions
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, IntegrationsConstants, Tokens, StatusCodes


@allure.epic("Test integrations")
@pytest.mark.auto_test
class TestIntegrations:
    const = IntegrationsConstants
    url = Urls
    token = Tokens
    page = RESTApi
    code = StatusCodes

    @allure.title('Проверка доступности MSPortal Test')
    def test_get_ms_portal_test(self):
        response_test = self.page.get(self.const.MS_URL_TEST, headers=self.token.MS_PROD)
        Assertions.assert_status_code(response_test, self.code.OK)

    @allure.title('Проверка доступности MSPortal Prod')
    def test_get_ms_portal_prod(self):
        response_prod = self.page.get(self.const.MS_URL_TEST, headers=self.token.MS_PROD)
        Assertions.assert_status_code(response_prod, self.code.OK)

    @allure.title('Получение данные качества тест MSPortal')
    def test_get_indicators_test(self):
        url = f'{self.const.MS_URL_TEST}resultByQuarter?year={self.const.YEAR}&quarter={self.const.QUARTER}'
        response_test = self.page.get(url=url, headers=self.token.MS_PROD)
        # dealers = [item['dealer_id'] for item in response_test.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на тесте ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [item['mark'] for item in response_test.json() if item['dealer_id'] == dealer], sep='\n')
        Assertions.assert_status_code(response_test, self.code.OK)

    @allure.title('Получить данные качества прод MSPortal')
    def test_get_indicators_prod(self):
        url = f'{self.const.MS_URL_PROD}resultByQuarter?year={self.const.YEAR - 1}&quarter={self.const.QUARTER + 3}'
        response_prod = self.page.get(url=url, headers=self.token.MS_PROD)
        # pprint(response_prod.json())
        # dealers = [item['dealer_id'] for item in response_prod.json()]
        # for dealer in dealers:
        #     print(f'\nСписок индикаторов для ДЦ {dealer} на прод ({self.const.QUARTER}Q{self.const.YEAR % 2000}):',
        #           [f"{item['mark']} = {item['kindForm']} + {item['typeForm']}" for item in response_prod.json()
        #            if item['dealer_id'] == dealer], sep='\n')
        Assertions.assert_status_code(response_prod, self.code.OK)

    @allure.title('Получить данные качества прод MSPortal kindForm')
    def test_get_kind_form_prod(self):
        url = f'{self.const.MS_URL_PROD}kindForm'
        response_prod = self.page.get(url=url, headers=self.token.MS_PROD)
        # pprint(response_prod.json())
        Assertions.assert_status_code(response_prod, self.code.OK)

    @allure.title('Получить данные качества прод MSPortal typeForm')
    def test_get_type_form(self):
        url = f'{self.const.MS_URL_PROD}typeForm'
        response_prod = self.page.get(url=url, headers=self.token.MS_PROD)
        # pprint(response_prod.json())
        Assertions.assert_status_code(response_prod, self.code.OK)

    @allure.title('Проверить доступности Candidates')
    def test_get_candidates_health(self):
        url = f'{self.url.CANDIDATES_URL}/health'
        response = self.page.get(url)
        # pprint(response.json())
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить ДЦ из Реестра')
    def test_get_registry_dealers(self):
        url = f'{self.url.REGISTRY_URL}/AVWS_PPD_REESTR_DLR'
        headers = self.token.REGISTRY
        response = self.page.get(url, headers=headers)
        # pprint(response.json())
        # print([(item['DEALER_ID'], item['PN_INFO']) for item in response.json() if item['DEALER_ID'] == 6427884196])
        # print()
        # print('DEALER_ID', 'DEALER_NAME', "DEALER_INN", "DEALER_FILIALCODE", 'UR_DIST_CODE')
        # pprint([(item['DEALER_ID'], item['DEALER_NAME'], item["DEALER_INN"], item["DEALER_FILIALCODE"],
        #          item['UR_DIST_CODE']) for item in response.json() if type(item['UR_DIST_CODE']) is not type(10)])
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить пользователей из Реестра')
    def test_get_registry_users(self):
        url = f'{self.url.REGISTRY_URL}/AVWS_PPD_USER_REESTR'
        headers = self.token.REGISTRY
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить чек-листы из autocrm (ПКД)')
    def test_pkd_integration(self):
        url = self.url.AUTOCRM_URL
        headers = self.token.AUTOCRM
        response = requests.get(url=url, headers=headers)
        # print([item["dealer_code"] for item in response.json()])
        Assertions.assert_status_code(response, self.code.OK)
