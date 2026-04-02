import allure
import pytest
import json
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


@allure.suite('Dealer')
@pytest.mark.manual_run
class TestDealer(TestApi):

    @allure.title('Получить базовую информацию дилера по айди')
    def test_get_dealer_base(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/base?id=1197057857'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @pytest.mark.skip
    @allure.title('Обновить базовую информацию дилера по айди')
    def test_put_dealer_base(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/base'
        headers = self.header.HEADERS_ADMIN
        payload = json.dumps({
            "id": 1197057857,
            'holdingName': 'Холдинг Авалон',
        })
        response = self.page.put(url=url, headers=headers, data=payload)
        # print(response.status_code)
        # pprint(response.json())
        Assertions.assert_status_code(response, self.code.OK)

    @pytest.mark.skip
    @allure.title('Создать нового дилера')
    def test_post_dealer_base(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/base'
        payload = json.dumps({
            "dealerName": "Новый Авалон 19.09.25",
            "code": "00",
            "inn": "12345678",
            "address": "Россия",
            "country": "Россия",
            "city": "Тольятти"
        })
        headers = self.header.HEADERS_ADMIN
        response = self.page.post(url=url, headers=headers, data=payload)
        Assertions.assert_status_code(response, self.code.CREATE)

    @allure.title('Получить информацию по адресам дилера')
    def test_get_dealer_address_id(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/address?id=1197057857'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @pytest.mark.skip
    @allure.title('Обновить информацию по адресам дилера')
    def test_put_dealer_address(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/address'
        headers = self.header.HEADERS_ADMIN
        payload = json.dumps({
            "id": 1691874934,
            "additional": {
                "legalAddress": {
                    "reestrLegalAddress": "МКАД 78 км,  д. 2, корп. 4, помещение 1",
                    'country': {'id': 20674},
                    'fo': {'id': 20681},
                    'subject': {'id': 30388},
                    'district': None,
                    'city': {'id': 30389},
                    'locality': {'id': 70767167},
                    'street': {'id': 36643189},
                    'house': {'id': 53359137}
                }
            }
        }
        )
        response = self.page.put(url=url, headers=headers, data=payload)
        Assertions.assert_status_code(response, self.code.CREATE)

    @allure.title('Получить информацию по документам ДЦ')
    def test_get_dealer_docs(self):
        url = f'{self.url.MAIN_URL}/internal-api/dealer/docs?id=1193537702'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url=url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

