from selenium.webdriver.common.by import By


class MainPageLocators:
    AGREE_BUTTON = (By.XPATH, '//span[text()="Согласен"]')
    ENTER_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    EDITOR_BUTTON = (By.XPATH, '//a[@href="/editor/"]')
    NOTIFICATIONS_BUTTON = (By.XPATH, '//div[contains(@class, "notifications")]')
    ERRORS = (By.XPATH, '//*[contains(text(), "error")]')
    FIND_DEALER = (By.CSS_SELECTOR, '.desc--2vJ input')
    SELECT_DEALERS = (By.CLASS_NAME, 'deaelers_container--3yC')

    SELECT_DEALER_BUTTON = (By.XPATH, '//span[text()="Выбрать дилера"]')
    PKD_BUTTON = (By.XPATH, '//span[text()="ПКД"]')
    INTERRUPTION_BUTTON = (By.XPATH, '//span[text()="Нарушения"]')
    NOTICES_BUTTON = (By.XPATH, '//span[text()="Объявления"]')
    DOCUMENTS_BUTTON = (By.XPATH, '//span[text()="Документы"]')
    ACCOUNTING_BUTTON = (By.XPATH, '//span[text()="Бухгалтерия"]')
    SRR_BUTTON = (By.XPATH, '//span[text()="SRR"]')
    REPORTS_BUTTON = (By.XPATH, '//span[text()="Отчеты"]')
    MENU = (By.CLASS_NAME, 'menu--1eR')

    BLOCK_ABOUT = (By.CLASS_NAME, 'about--1Vq')
    BLOCK_ABOUT_BUTTONS = (By.CLASS_NAME, 'linkWrapper--38R')
