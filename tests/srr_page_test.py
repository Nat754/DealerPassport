import allure
import pytest
from pages.srr_page import SRRPage
from tests.constants import SRRConstant, Urls


@allure.epic("Test SRR Page smoke_test")
@pytest.mark.smoke_test
class TestSRRPageSmoke:

    @allure.title(f'Проверить доступность списка групп отчетов SRR на prod')
    def test_open_srr_group_reports_prod(self, auth_user_admin_to_prod, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL_PROD + Urls.SRR_URL)
        assert page.check_group_record_select() == SRRConstant.LIST_GROUPS, 'Список групп отчетов SRR изменился'

    @allure.title(f'Проверить формирование отчета SRR в файл excell на prod')
    def test_report_srr_prod_excell(self, auth_user_admin_to_prod, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL_PROD + Urls.SRR_URL)
        page.check_params_is_visible().click()
        page.check_excell_button_is_visible().click()
        assert auth_user_admin_to_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_prod.check_error_notifications()]}'

    @allure.title(f'Проверить формирование отчета SRR на экране на prod')
    def test_report_srr_prod_create(self, auth_user_admin_to_prod, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL_PROD + Urls.SRR_URL)
        page.check_params_is_visible().click()
        page.check_create_button_is_visible().click()
        assert auth_user_admin_to_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_prod.check_error_notifications()]}'

    @allure.title(f'Проверить формирование отчета SRR в файл excell и на экран на seo prod')
    def test_report_srr_seo_prod_excell(self, auth_user_admin_to_seo_prod, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL_SEO_PROD + Urls.SRR_URL)
        page.check_params_is_visible().click()
        page.check_excell_button_is_visible().click()
        page.check_create_button_is_visible().click()
        assert auth_user_admin_to_seo_prod.check_not_errors(), \
            f'Ошибка: {[item.text for item in auth_user_admin_to_seo_prod.check_error_notifications()]}'

    @allure.title(f'Проверить текст в модальном окне prod')
    def test_text_srr_seo_prod(self, auth_user_admin_to_prod, driver):
        page = SRRPage(driver)
        driver.get(Urls.MAIN_URL_PROD + Urls.SRR_URL)
        page.check_params_is_visible().click()
        title = page.get_title_modal().text
        assert title == SRRConstant.TEXT_TITLE_MODAL, \
            f'ОР: {SRRConstant.TEXT_TITLE_MODAL}, ФР: {title}'
