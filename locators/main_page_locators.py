from selenium.webdriver.common.by import By


class MainPageLocators:
    AGREE_BUTTON = (By.XPATH, '//span[text()="Согласен"]')
    ENTER_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    EDITOR_BUTTON = (By.XPATH, '//a[@href="/editor/"]')
    CHOOSE_DEALER_BUTTON = (By.XPATH, '//button[contains(@class, "dealer")]')
    PKD_BUTTON = (By.XPATH, '//span[text()="ПКД"]')
    INTERRUPTION_BUTTON = (By.XPATH, '//span[text()="Нарушения"]')
    NOTICES_BUTTON = (By.XPATH, '//span[text()="Объявления"]')
    DOCUMENTS_BUTTON = (By.XPATH, '//span[text()="Документы"]')
    ACCOUNTING_BUTTON = (By.XPATH, '//span[text()="Бухгалтерия"]')
    SRR_BUTTON = (By.XPATH, '//span[text()="SRR"]')
    REPORTS_BUTTON = (By.XPATH, '//span[text()="Отчеты"]')
    NOTIFICATIONS = (By.XPATH, '//div[contains(@class, "notifications")]')
    ERRORS = (By.XPATH, '//*[contains(text(), "error")]')
