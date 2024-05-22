from pages.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locator = MainPageLocators

    @allure.step(f"Проверка видимости кнопки '{locator.ENTER_BUTTON}' на главной странице")
    def check_button_enter(self):
        return self.element_is_visible(self.locator.ENTER_BUTTON)

    @allure.step(f"Проверка видимости кнопки '{locator.AGREE_BUTTON}' на главной странице")
    def check_button_agree(self):
        return self.element_is_visible(self.locator.AGREE_BUTTON)

    @allure.step(f"Проверить видимость ошибок")
    def check_error_notifications(self):
        return self.elements_are_visible(self.locator.NOTIFICATIONS)

    @allure.step(f"Проверить отсутствие ошибок")
    def check_not_errors(self):
        return self.elements_are_not_visible(self.locator.NOTIFICATIONS)

    @allure.step(f"Проверка кликабельности кнопки '{locator.EDITOR_BUTTON}' на главной странице")
    def check_button_editor(self):
        return self.element_is_clickable(self.locator.EDITOR_BUTTON)

    @allure.step(f"Проверка кликабельности кнопки '{locator.CHOOSE_DEALER_BUTTON}' на главной странице")
    def check_button_choose_dealer(self):
        return self.element_is_clickable(self.locator.CHOOSE_DEALER_BUTTON)

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
