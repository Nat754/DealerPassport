from selenium.webdriver.common.by import By


class SRRPageLocators:
    GROUP_REPORT_SELECT = (By.XPATH, '(//div[@class=" css-peenyy-control"])[1]')
    GROUP_REPORT_SELECT2 = (By.XPATH, '(//div[@class=" css-peenyy-control"])[2]')
    LIST_REPORT_SELECT = (By.XPATH, '//div[contains(@class, "-menu")]')
    REPORT_SELECT = (By.XPATH, '(//div[@class=" css-peenyy-control"])[2]')
    PARAMS = (By.XPATH, '//button[contains(@class, "green")]')
    EXCELL_REPORT = (By.XPATH, '(//button[@type="submit"])[1]')
    CREATE_REPORT = (By.XPATH, '(//button[@type="submit"])[2]')
    TITLE_MODAL = (By.XPATH, '(//div[contains(@class, "title")])[1]')
    SUB_MENU_SELECT_0 = (By.ID, 'react-select-3-option-0')
    SUB_MENU_SELECT_1 = (By.ID, 'react-select-3-option-1')
    SUB_MENU_SELECT_2 = (By.ID, 'react-select-3-option-2')
    SUB_MENU_SELECT_3 = (By.ID, 'react-select-3-option-3')
