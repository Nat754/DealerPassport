from pprint import pprint
import allure
import pytest
from pages.ms_page import MSPortal
from tests.constants import Urls, MSConstants, Tokens


@allure.epic("Test integration with MSPortal")
@pytest.mark.auto_test
class TestQuality:
    ms = MSConstants
    url = Urls
    header = Tokens
    page = MSPortal()

    @allure.title('Проверка доступности MSPortal')
    def test_get_status_code(self):
        response_test = self.page.get_quality(self.ms.url_test, Tokens.MS_PROD)
        response_prod = self.page.get_quality(self.ms.url_prod, Tokens.MS_PROD)
        assert response_test.status_code == 200, 'Неверный ответ сервера'
        assert response_prod.status_code == 200, 'Неверный ответ сервера'

    @allure.title('Получение данных тест MSPortal')
    def test_get_indicators_test(self):
        response_test = self.page.get_quality(self.ms.url_test, Tokens.MS_PROD).json()
        dealers = [item['dealer_id'] for item in response_test]
        # print('List of dealers on test:', dealers, sep='\n')
        for dealer in dealers:
            print(f'\nСписок индикаторов для дилера {dealer} на тесте ({self.ms.QUARTER}Q{self.ms.YEAR % 2000}):',
                  [item['mark'] for item in response_test if item['dealer_id'] == dealer], sep='\n')
            # self.ms.DEALER_ID], sep='\n')
        pprint(response_test)

    @allure.title('Получение данных прод MSPortal')
    def test_get_indicators_prod(self):
        response_prod = self.page.get_quality(self.ms.url_prod, Tokens.MS_PROD).json()
        dealers = [item['dealer_id'] for item in response_prod]
        # print('List of dealers on prod:', dealers, sep='\n')
        for dealer in dealers:
            print(f'\nСписок индикаторов для дилера {dealer} на проде ({self.ms.QUARTER}Q{self.ms.YEAR % 2000}):',
                  [item['mark'] for item in response_prod if item['dealer_id'] == dealer], sep='\n')
            # self.ms.DEALER_ID], sep='\n')
        # pprint(response_prod)


# url = "https://ms-n-back.vaz.ru/api/v1/form/kindForm"
#
# payload = {}
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvdHBvcnRhbC52YXoucnUiLCJhdWQiOiJodHRwOlwvXC9tcm0uc2VvdGx0LnJ1XC9hcGlcL3YxXC9hdXRoIiwiaWF0IjoxMzU2OTk5NTI0LCJuYmYiOjEzNTY5OTk1MjQsImRhdGEiOnsibG9nbmFtZSI6ImdlaDEiLCJlbnlkYXRhIjoiSEZXa2VDYmRRZmtFYXpPcUt3YkRLUDQ2UThvZHhXUFR1VkM3V2c3V243VVFSU2Izd3ZHTEgrTHQ2Um03Z3pXeEJtZlJ2NzN4bTN6QkNZZDFKYlwvOGRNTUM2U2Z5Nlc0dWVhSmVKNktLVVdHdmxaQ0QrN0xkXC9OS2kxU3h5eDNRQVhkeE81bk05OTJReEI4T0Y4OGpGQnRRSGdpaUY1ZDZuZnRiRnJ6ZVg2MGc9In19._QWPBIWAwQOQ6ppPfRT7Pv9SLqILpK1bTeGXYiH0Sk4'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
