import allure
import pytest
from pages.srr_page import SRRPage
from tests.constants import SRRConstant, Urls


@allure.epic("Тестирование страницы отчетов SRR")
@pytest.mark.auto_test
class TestSRRPageSmoke:

    @allure.title('Проверить доступность списка групп отчетов SRR')
    def test_open_srr_group_reports(self, auth_user_admin, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL + Urls.SRR_URL)
        assert page.check_group_record_select() == SRRConstant.LIST_GROUPS, 'Список групп отчетов SRR изменился'

    @allure.title('Проверить формирование отчета SRR в файл excell')
    def test_report_srr_to_excell(self, auth_user_admin, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL + Urls.SRR_URL)
        page.check_params_is_visible().click()
        page.check_excell_button_is_visible().click()
        assert auth_user_admin.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin.check_error_notifications()]}'

    @allure.title('Проверить формирование отчета SRR на экране')
    def test_report_srr_create(self, auth_user_admin, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL + Urls.SRR_URL)
        page.check_params_is_visible().click()
        page.check_create_button_is_visible().click()
        assert auth_user_admin.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin.check_error_notifications()]}'

    @allure.title('Проверить текст в модальном окне')
    def test_text_srr(self, auth_user_admin, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL + Urls.SRR_URL)
        page.check_params_is_visible().click()
        title = page.get_title_modal().text
        assert title == SRRConstant.TEXT_TITLE_MODAL, \
            f'ОР: {SRRConstant.TEXT_TITLE_MODAL}, ФР: {title}'
