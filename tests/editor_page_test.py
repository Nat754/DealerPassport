import pytest
import allure
from tests.constants import Urls, EditorConstants
from pages.editor_page import EditorPage


@allure.epic("Test SRR Page smoke_test")
@pytest.mark.smoke_test
class TestEditorPageSmoke:

    @allure.title('Проверить доступность меню в редакторе на prod')
    def test_editor_menu_prod(self, auth_user_admin_to_prod, driver):
        driver.get(Urls.MAIN_URL_PROD + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU_PROD, 'Меню редактора изменилось'
