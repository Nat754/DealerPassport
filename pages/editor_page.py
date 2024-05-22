from pages.base_page import BasePage
import allure
from locators.editor_page_locators import EditorPageLocators


class EditorPage(BasePage):
    locator = EditorPageLocators()

    @allure.step(f"Проверка видимости групп в Редакторе")
    def check_groups_editor(self):
        editor_menu = self.elements_are_visible(self.locator.ITEMS_LIST)
        items_list = [item.text for item in editor_menu]
        return items_list

