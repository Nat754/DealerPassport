import pytest
import allure
from tests.constants import Urls, EditorConstants
from pages.editor_page import EditorPage


@allure.epic("Test SRR Page smoke_test")
@pytest.mark.smoke_test
class TestEditorPageSmoke:

    @allure.title(f'Проверить доступность меню в редакторе на seo')
    def test_editor_menu_seo(self, auth_user_admin_to_seo, driver):
        driver.get(Urls.MAIN_URL_SEO + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU_SEO, 'Меню редактора изменилось'

    @allure.title(f'Проверить доступность меню в редакторе на seo prod')
    def test_editor_menu_seo_prod(self, auth_user_admin_to_seo_prod, driver):
        driver.get(Urls.MAIN_URL_SEO_PROD + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU_SEO_PROD, 'Меню редактора изменилось'

    @pytest.mark.xfail
    @allure.title(f'Проверить доступность меню в редакторе на prod')
    def test_editor_menu_prod(self, auth_user_admin_to_prod, driver):
        driver.get(Urls.MAIN_URL_PROD + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU_PROD, 'Меню редактора изменилось'

    @pytest.mark.skip
    @allure.title(f'Проверить доступность меню в редакторе на test')
    def test_editor_menu_test(self, auth_user_admin_to_prod, driver):
        driver.get(Urls.MAIN_URL_PROD + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU_SEO_PROD, 'Меню редактора изменилось'
