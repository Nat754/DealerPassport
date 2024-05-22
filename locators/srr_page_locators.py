from selenium.webdriver.common.by import By


class SRRPageLocators:
    GROUP_REPORT_SELECT = (By.XPATH, '(//div[@class=" css-peenyy-control"])[1]')
    LIST_REPORT_SELECT = (By.XPATH, '//div[contains(@class, "-menu")]')
    REPORT_SELECT = (By.XPATH, '(//div[@class=" css-peenyy-control"])[2]')
    PARAMS = (By.XPATH, '//button[contains(@class, "green")]')
    EXCELL_REPORT = (By.XPATH, '(//button[@type="submit"])[1]')
    CREATE_REPORT = (By.XPATH, '(//button[@type="submit"])[2]')
    TITLE_MODAL = (By.XPATH, '(//div[contains(@class, "title")])[1]')
