import pytest
import allure
from tests.constants import Urls, EditorConstants
from pages.editor_page import EditorPage


@allure.epic("Тестирование страницы 'Редактор'")
@pytest.mark.auto_test
class TestEditorPage:

    @allure.title('Проверить доступность меню в редакторе')
    def test_editor_menu(self, auth_user_admin, driver):
        driver.get(Urls.MAIN_URL + Urls.EDITOR_URL)
        page = EditorPage(driver)
        assert page.check_groups_editor() == EditorConstants.EDITOR_MENU, 'Меню редактора изменилось'
