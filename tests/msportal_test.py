# from pprint import pprint
import allure
from pages.ms_page import MSPortal
from tests.constants import Urls, MSConstants, Tokens


@allure.epic("Test integration with MSPortal")
class TestQuality:
    ms = MSConstants
    url = Urls
    header = Tokens
    page = MSPortal()

    @allure.title('Проверка доступности MSPortal')
    def test_get_status_code(self):
        response_test = self.page.get_quality(self.ms.url_test, Tokens.MS_TEST)
        response_prod = self.page.get_quality(self.ms.url_prod, Tokens.MS_PROD)
        assert response_test.status_code == 200, 'Неверный ответ сервера'
        assert response_prod.status_code == 200, 'Неверный ответ сервера'

    @allure.title('Получение данных тест MSPortal')
    def test_get_indicators_test(self):
        response_test = self.page.get_quality(self.ms.url_test, Tokens.MS_TEST).json()

        # print('List of dealers on test:', [item['dealer_id'] for item in response_test], sep='\n')
        print(f'\nСписок индикаторов для дилера {self.ms.DEALER_ID} на тесте ({self.ms.QUARTER}Q{self.ms.YEAR % 2000}):',
              [item['mark'] for item in response_test if item['dealer_id'] == self.ms.DEALER_ID], sep='\n')
        # pprint(response_test)

    @allure.title('Получение данных прод MSPortal')
    def test_get_indicators_prod(self):
        response_prod = self.page.get_quality(self.ms.url_prod, Tokens.MS_PROD).json()
        # print('The list of dealers from prod_admin:', [item['dealer_id'] for item in response_prod], sep='\n')
        print(f'\nСписок индикаторов для дилера {self.ms.DEALER_ID} на проде ({self.ms.QUARTER}Q{self.ms.YEAR % 2000}):',
              [item['mark'] for item in response_prod if item['dealer_id'] == self.ms.DEALER_ID], sep='\n')
        # pprint(response_prod)
