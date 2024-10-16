from tests.constants import SRRConstant
from pages.base_page import BasePage
import allure
from locators.srr_page_locators import SRRPageLocators


class SRRPage(BasePage):
    locator = SRRPageLocators()
    srr_const = SRRConstant()

    @allure.step("Проверка видимости выбора группы отчетов SRR")
    def check_group_record_select(self):
        self.element_is_visible(self.locator.GROUP_REPORT_SELECT).click()
        list_groups_of_reports = [item.text for item in self.elements_are_present(self.locator.LIST_REPORT_SELECT)]
        return list_groups_of_reports

    @allure.step(f"Проверка видимости кнопки '{srr_const.TEXT_PARAM_BUTTON}'")
    def check_params_is_visible(self):
        return self.element_is_visible(self.locator.PARAMS)

    @allure.step(f"Проверка видимости кнопки '{srr_const.TEXT_REPORT_EXCELL}'")
    def check_excell_button_is_visible(self):
        return self.element_is_visible(self.locator.EXCELL_REPORT)

    @allure.step(f"Проверка видимости кнопки '{srr_const.TEXT_REPORT_CREATE}'")
    def check_create_button_is_visible(self):
        return self.element_is_visible(self.locator.CREATE_REPORT)

    @allure.step(f"Проверка видимости заголовка '{srr_const.TEXT_TITLE_MODAL}'")
    def get_title_modal(self):
        return self.element_is_visible(self.locator.TITLE_MODAL)

    @allure.step("Выбрать подгруппу отчетов")
    def check_subgroup_record_select(self):
        return self.element_is_visible(self.locator.GROUP_REPORT_SELECT2).click()

    @allure.step("Выбрать подотчет")
    def get_sub_menu(self, n):
        return self.element_is_visible(("id", f'react-select-3-option-{n}')).text
