import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class Tokens:

    TOKEN_SEO = {'token': f'{os.environ["SEO_ADMIN"]}'}
    TOKEN_TEST = {'Authorization': f'{os.environ["TEST_ADMIN"]}'}
    TOKEN_PROD = {'Authorization': f'{os.environ["PROD_ADMIN"]}'}
    MS_PROD = {'Authorization': f'{os.environ["MS_PROD"]}'}
    MS_TEST = {'Authorization': f'{os.environ["MS_TEST"]}'}


class Urls:
    AUTH = "/auth"
    EDITOR_URL = "/editor/"
    REPORTS_URL = "/reports/"
    LOGS_URL = "/logs/"
    SRR_URL = "/srr/"
    ACCOUNTING_URL = "/accounting/"
    DOCUMENTS_URL = "/documents/"
    ZD_URL = "/zd/"
    GR_URL = "/gr/"
    Q_URL = "/q/"
    STAFF_URL = "/staff/"
    DEALERS_URL = "/dealers/"
    USERS_URL = "/users/"
    INDICATORS_URL = "/indicators/"
    UPLOADS_URL = "/uploads/"
    MAIN_URL_SEO = os.environ["MAIN_URL_SEO"]
    MAIN_URL_SEO_PROD = MAIN_URL_SEO + ":3001"
    MAIN_URL_TEST = os.environ["MAIN_URL_TEST"]
    MAIN_URL_PROD = os.environ["MAIN_URL_PROD"]
    MS_URL_TEST = os.environ["MS_URL_TEST"]
    MS_URL_PROD = os.environ["MS_URL_PROD"]

    LIST_URLS_SEO = [MAIN_URL_SEO,
                     MAIN_URL_SEO + EDITOR_URL,
                     MAIN_URL_SEO + REPORTS_URL,
                     MAIN_URL_SEO + LOGS_URL,
                     MAIN_URL_SEO + SRR_URL,
                     MAIN_URL_SEO + ACCOUNTING_URL,
                     MAIN_URL_SEO + DOCUMENTS_URL,
                     MAIN_URL_SEO + ZD_URL,
                     MAIN_URL_SEO + GR_URL,
                     MAIN_URL_SEO + Q_URL,
                     MAIN_URL_SEO + STAFF_URL,
                     MAIN_URL_SEO + DEALERS_URL,
                     MAIN_URL_SEO + USERS_URL,
                     MAIN_URL_SEO + INDICATORS_URL,
                     MAIN_URL_SEO + UPLOADS_URL]

    LIST_URLS_SEO_PROD = [MAIN_URL_SEO_PROD,
                          MAIN_URL_SEO_PROD + EDITOR_URL,
                          MAIN_URL_SEO_PROD + REPORTS_URL,
                          MAIN_URL_SEO_PROD + LOGS_URL,
                          MAIN_URL_SEO_PROD + SRR_URL,
                          MAIN_URL_SEO_PROD + ACCOUNTING_URL,
                          MAIN_URL_SEO_PROD + DOCUMENTS_URL,
                          MAIN_URL_SEO_PROD + ZD_URL,
                          MAIN_URL_SEO_PROD + GR_URL,
                          MAIN_URL_SEO_PROD + Q_URL,
                          MAIN_URL_SEO_PROD + STAFF_URL,
                          MAIN_URL_SEO_PROD + DEALERS_URL,
                          MAIN_URL_SEO_PROD + USERS_URL,
                          MAIN_URL_SEO_PROD + INDICATORS_URL,
                          MAIN_URL_SEO_PROD + UPLOADS_URL]

    LIST_URLS_PROD = [MAIN_URL_PROD,
                      MAIN_URL_PROD + EDITOR_URL,
                      MAIN_URL_PROD + REPORTS_URL,
                      MAIN_URL_PROD + LOGS_URL,
                      MAIN_URL_PROD + SRR_URL,
                      MAIN_URL_PROD + ACCOUNTING_URL,
                      MAIN_URL_PROD + DOCUMENTS_URL,
                      MAIN_URL_PROD + ZD_URL,
                      MAIN_URL_PROD + GR_URL,
                      MAIN_URL_PROD + Q_URL,
                      MAIN_URL_PROD + STAFF_URL,
                      MAIN_URL_PROD + DEALERS_URL,
                      MAIN_URL_PROD + USERS_URL,
                      MAIN_URL_PROD + INDICATORS_URL,
                      MAIN_URL_PROD + UPLOADS_URL]

    LIST_URLS_TEST = [MAIN_URL_TEST,
                      MAIN_URL_TEST + EDITOR_URL,
                      MAIN_URL_TEST + REPORTS_URL,
                      MAIN_URL_TEST + LOGS_URL,
                      MAIN_URL_TEST + SRR_URL,
                      MAIN_URL_TEST + ACCOUNTING_URL,
                      MAIN_URL_TEST + DOCUMENTS_URL,
                      MAIN_URL_TEST + ZD_URL,
                      MAIN_URL_TEST + GR_URL,
                      MAIN_URL_TEST + Q_URL,
                      MAIN_URL_TEST + STAFF_URL,
                      MAIN_URL_TEST + DEALERS_URL,
                      MAIN_URL_TEST + USERS_URL,
                      MAIN_URL_TEST + INDICATORS_URL,
                      MAIN_URL_TEST + UPLOADS_URL]


class SRRConstant:
    LIST_GROUPS = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по периоду '
                   'продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение автомобилей '
                   'на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в динамике\nМашинозаезды по '
                   'дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты не обращавшиеся на гарантийный'
                   ' ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация ГИБДД\n1С УПП']
    TEXT_PARAM_BUTTON = 'Параметры'
    TEXT_REPORT_CREATE = 'Сформировать'
    TEXT_REPORT_EXCELL = 'Сохр. в excel'
    TEXT_TITLE_MODAL = 'ОТЧЕТ ВОЗВРАЩЕНИЕ АВТОМОБИЛЕЙ НА ТО (СВОЙ) ПО МЕСЯЦУ КОНТРОЛЯ'
    SRR = ['Возвращение автомобилей на ТО (свой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой-чужой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой - чужой) по месяцу контроля по семейству автомобилей',
           'Возвращение автомобилей на ТО (семейство автомобиля - регион)']


class EditorConstants:
    EDITOR_MENU_PROD = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
                        'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
                        'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
                        'Справочник информационных систем']
    EDITOR_MENU_SEO = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
                       'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
                       'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
                       'Справочник зон камер', 'Справочник информационных систем',
                       'Справочник разделов фотогалереи', 'Шаблоны договоров']
    EDITOR_MENU_SEO_PROD = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
                            'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
                            'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
                            'Справочник зон камер', 'Справочник информационных систем',
                            'Справочник разделов фотогалереи', 'Шаблоны договоров']


class MSConstants:
    YEAR = datetime.now().year
    QUARTER = (datetime.now().month - 1) // 3
    DEALER_ID = '1197057857'
    url_test = f'{Urls.MS_URL_TEST}?year={YEAR}&quarter={QUARTER}'
    url_prod = f'{Urls.MS_URL_PROD}?year={YEAR}&quarter={QUARTER}'
