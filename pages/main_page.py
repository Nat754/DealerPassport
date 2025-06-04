import time
from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from tests.constants import HeaderConstant


class MainPage(BasePage):
    locator = MainPageLocators
    hconstant = HeaderConstant

    @allure.step(f"Проверка видимости кнопки '{locator.ENTER_BUTTON}' на главной странице")
    def check_button_enter(self):
        return self.element_is_visible(self.locator.ENTER_BUTTON)

    @allure.step(f"Проверка видимости кнопки '{locator.AGREE_BUTTON}' на главной странице")
    def check_button_agree(self):
        return self.element_is_visible(self.locator.AGREE_BUTTON)

    @allure.step("Проверить видимость ошибок")
    def check_error_notifications(self):
        return self.elements_are_visible(self.locator.NOTIFICATIONS_BUTTON)

    @allure.step("Проверить отсутствие ошибок")
    def check_not_errors(self):
        return self.elements_are_not_visible(self.locator.NOTIFICATIONS_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.EDITOR_BUTTON}' на главной странице")
    def check_button_editor(self):
        return self.element_is_clickable(self.locator.EDITOR_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{hconstant.SELECT_DEALER_TEXT}' на главной странице")
    def check_button_select_dealer(self):
        return self.element_is_clickable(self.locator.SELECT_DEALER_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.PKD_BUTTON}' на главной странице")
    def check_button_pkd(self):
        return self.element_is_clickable(self.locator.PKD_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.INTERRUPTION_BUTTON}' на главной странице")
    def check_button_interruption(self):
        return self.element_is_clickable(self.locator.INTERRUPTION_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.NOTICES_BUTTON}' на главной странице")
    def check_button_notices(self):
        return self.element_is_clickable(self.locator.NOTICES_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.DOCUMENTS_BUTTON}' на главной странице")
    def check_button_documents(self):
        return self.element_is_clickable(self.locator.DOCUMENTS_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.ACCOUNTING_BUTTON}' на главной странице")
    def check_button_accounting(self):
        return self.element_is_clickable(self.locator.ACCOUNTING_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.SRR_BUTTON}' на главной странице")
    def check_button_srr(self):
        return self.element_is_clickable(self.locator.SRR_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.REPORTS_BUTTON}' на главной странице")
    def check_button_reports(self):
        return self.element_is_clickable(self.locator.REPORTS_BUTTON)

    @allure.step("Ввести имя дилера в поисковой строке")
    def check_select_find_dealer(self, name):
        self.element_is_visible(self.locator.FIND_DEALER).click()
        return self.element_is_visible(self.locator.FIND_DEALER).send_keys(name)

    @allure.step("Получить список дилеров")
    def check_select_dealers(self):
        loader = self.elements_are_visible(self.locator.SELECT_DEALERS)[0].text
        while loader == [self.hconstant.LOADER_MSG]:
            loader = self.elements_are_visible(self.locator.SELECT_DEALERS)[0].text
        time.sleep(2)
        dealers = self.elements_are_visible(self.locator.SELECT_DEALERS)[0].text.split('\n')
        return dealers

    @allure.step("Проверка отображения меню в шапке портала")
    def check_menu(self):
        return self.elements_are_visible(self.locator.MENU)

    @allure.step("Проверка отображения информации о ДЦ")
    def check_block_about(self):
        return self.element_is_visible(self.locator.BLOCK_ABOUT)

    @allure.step(f"Проверка видимости кнопок в блоке информации о ДЦ")
    def check_block_about_buttons(self):
        return self.elements_are_visible(self.locator.BLOCK_ABOUT_BUTTONS)
