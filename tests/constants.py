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
    PKD = {'Authorization': f'{os.environ["AUTOCRM"]}'}


class Urls:
    AUTH = "/auth"
    EDITOR_URL = "/editor/"
    REPORTS_URL = "/reports/"
    LOGS_URL = "/logs/"
    EMAIL_LOGS_URL = "/logs/email"
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
    MAIN_URL = os.environ["MAIN_URL_PROD"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ":3001"
    # MAIN_URL = os.environ["MAIN_URL_TEST"]
    MS_URL_TEST = os.environ["MS_URL_TEST"]
    MS_URL_PROD = os.environ["MS_URL_PROD"]
    LIST_URLS = [MAIN_URL,
                 MAIN_URL + EDITOR_URL,
                 MAIN_URL + REPORTS_URL,
                 MAIN_URL + LOGS_URL,
                 MAIN_URL + EMAIL_LOGS_URL,
                 MAIN_URL + SRR_URL,
                 MAIN_URL + ACCOUNTING_URL,
                 MAIN_URL + DOCUMENTS_URL,
                 MAIN_URL + ZD_URL,
                 MAIN_URL + GR_URL,
                 MAIN_URL + Q_URL,
                 MAIN_URL + STAFF_URL,
                 MAIN_URL + DEALERS_URL,
                 MAIN_URL + USERS_URL,
                 MAIN_URL + INDICATORS_URL,
                 MAIN_URL + UPLOADS_URL]


class SRRConstant:
    # for prod
    LIST_GROUPS = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по периоду '
                   'продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение автомобилей '
                   'на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в динамике\nМашинозаезды по '
                   'дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты не обращавшиеся на гарантийный'
                   ' ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация ГИБДД\n1С УПП']
    # for dev
    # LIST_GROUPS = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по периоду '
    #                'продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение автомобилей '
    #                'на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в динамике\nМашинозаезды по '
    #                'дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты не обращавшиеся на гарантийный'
    #                ' ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация ГИБДД\nUVIN\nNS\n1С УПП']
    TEXT_PARAM_BUTTON = 'Параметры'
    TEXT_REPORT_CREATE = 'Сформировать'
    TEXT_REPORT_EXCELL = 'Сохр. в excel'
    TEXT_TITLE_MODAL = 'ОТЧЕТ ВОЗВРАЩЕНИЕ АВТОМОБИЛЕЙ НА ТО (СВОЙ) ПО МЕСЯЦУ КОНТРОЛЯ'
    SRR = ['Возвращение автомобилей на ТО (свой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой-чужой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой - чужой) по месяцу контроля по семейству автомобилей',
           'Возвращение автомобилей на ТО (семейство автомобиля - регион)']


class EditorConstants:
    # for prod
    EDITOR_MENU = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения', 'Виды нарушений',
                   'Редактор форм заявок-деклараций', 'Справочник должностей', 'Каталог учебных программ',
                   'Справочники библиотеки документов', 'Редактор отчетов', 'Справочник информационных систем',
                   'Справочник разделов фотогалереи', 'Справочник для выбора адреса'] # prod
    # for dev
    # EDITOR_MENU = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
    #                'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
    #                'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
    #                'Справочник зон камер', 'Справочник информационных систем',
    #                'Справочник разделов фотогалереи', 'Шаблоны договоров', 'Справочник для выбора адреса',
    #                'Справочник доверенных лиц']


class MSConstants:
    YEAR = datetime.now().year
    QUARTER = (datetime.now().month - 1) // 3
    DEALER_ID = '1197057857'
    url_test = f'{Urls.MS_URL_TEST}?year={YEAR}&quarter={QUARTER}'
    url_prod = f'{Urls.MS_URL_PROD}?year={YEAR}&quarter={QUARTER}'


class HeaderConstant:
    EDITOR_BUTTON_TEXT = ''
    SELECT_DEALER_TEXT = 'ВЫБРАТЬ ДИЛЕРА'
    PKD_TEXT = ''
    INTERRUPTION_TEXT = ''
    NOTICES_TEXT = ''
    DOCUMENTS_TEXT = ''
    ACCOUNTING_TEXT = ''
    SRR_TEXT = ''
    REPORTS_TEXT = ''
    DEALER_NAME = ('ПИТЕР')
    LOADER_MSG = 'ЗАГРУЗКА...'
