import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class Urls:
    MAIN_URL = os.environ["MAIN_URL_PROD"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3001'
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3011'
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3012'
    # MAIN_URL = os.environ["MAIN_URL_TEST"]
    MS_URL_TEST = os.environ["MS_URL_TEST"]
    MS_URL_PROD = os.environ["MS_URL_PROD"]
    CANDIDATES_URL = os.environ["CANDIDATES_URL"]
    REGISTRY_URL = os.environ["REGISTRY_URL"]

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
    PKD_URL = "/pkd/"
    PKD_INDICATORS_URL = "/pkd/indicators/"
    PKD_CHECKLISTS_URL = "/pkd/checklists/"
    INTERRUPTION_URL = "/violations/"
    NOTICES_URL = "/announcement/"
    PASSPORT_BUTTON = MAIN_URL
    STAFF_CHECKED_URL = '/base/staff/?searchText=&page=0&openModal=&dateBegin=&selectedDate=&currentId='

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
                 MAIN_URL + UPLOADS_URL,
                 MAIN_URL + PKD_URL,
                 MAIN_URL + PKD_INDICATORS_URL,
                 MAIN_URL + PKD_CHECKLISTS_URL,
                 MAIN_URL + INTERRUPTION_URL,
                 MAIN_URL + NOTICES_URL,
                 MAIN_URL + STAFF_CHECKED_URL]


class Tokens:

    TOKEN = os.environ["PROD_ADMIN"] if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] else os.environ["TEST_ADMIN"]\
        if Urls.MAIN_URL == os.environ["MAIN_URL_TEST"] else os.environ["SEO_ADMIN"]
    TOKEN_TEST = os.environ["SEO_TEST"]
    TOKEN_EXPORT = os.environ["EXPORT_API_PROD"] if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"]\
        else os.environ["EXPORT_API_SEO"]
    TOKEN_ADMIN = {'token': TOKEN}
    MS_PROD = {'Authorization': f'{os.environ["MS_PROD"]}'}
    MS_TEST = {'Authorization': f'{os.environ["MS_TEST"]}'}
    PKD = {'Authorization': f'{os.environ["AUTOCRM"]}'}
    REGISTRY = {'Authorization': f'{os.environ["REGISTRY"]}'}
    MY_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImxvZ25hbWUiOiJTVVBFUl9BRE1JTiJ9LCJpYXQiOjE2OTA0Njk2MTJ9.f3kv5zYaDTvEYhfB9N5Nw8egdhfMGJBmxnas_5nCvzU'


class SRRConstant:

    LIST_PROD = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по периоду '
                 'продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение автомобилей '
                 'на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в динамике\nМашинозаезды по '
                 'дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты не обращавшиеся на гарантийный'
                 ' ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация ГИБДД\n1С УПП']

    LIST_DEV = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по'
                ' периоду продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение'
                ' автомобилей на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в'
                ' динамике\nМашинозаезды по дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты'
                ' не обращавшиеся на гарантийный ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация'
                ' ГИБДД\nUVIN\nNS\n1С УПП']

    LIST_GROUPS = LIST_PROD if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] else LIST_DEV

    TEXT_PARAM_BUTTON = 'Параметры'
    TEXT_REPORT_CREATE = 'Сформировать'
    TEXT_REPORT_EXCELL = 'Сохр. в excel'
    TEXT_TITLE_MODAL = 'ОТЧЕТ ВОЗВРАЩЕНИЕ АВТОМОБИЛЕЙ НА ТО (СВОЙ) ПО МЕСЯЦУ КОНТРОЛЯ'

    SRR = ['Возвращение автомобилей на ТО (свой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой-чужой) по месяцу контроля',
           'Возвращение автомобилей на ТО (свой - чужой) по месяцу контроля по семейству автомобилей',
           'Возвращение автомобилей на ТО (семейство автомобиля - регион)']


class EditorConstants:

    EDITOR_PROD = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения', 'Виды нарушений',
                   'Редактор форм заявок-деклараций', 'Справочник должностей', 'Каталог учебных программ',
                   'Справочники библиотеки документов', 'Редактор отчетов', 'Справочник информационных систем',
                   'Справочник разделов фотогалереи', 'Справочник для выбора адреса', 'Справочник тарифов IVIDEON',
                   'Реквизиты АВТОВАЗ']

    EDITOR_DEV = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
                  'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
                  'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
                  'Справочник зон камер', 'Справочник информационных систем',
                  'Справочник разделов фотогалереи', 'Шаблоны договоров', 'Справочник для выбора адреса',
                  'Справочник доверенных лиц', 'Справочник тарифов IVIDEON', 'Реквизиты АВТОВАЗ']

    EDITOR_MENU = EDITOR_PROD if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] else EDITOR_DEV


class IntegrationsConstants:
    YEAR = datetime.now().year
    QUARTER = datetime.now().month // 3
    MONTH = datetime.now().month
    DATE_NOW = datetime.now().date()
    DEALER_ID = '1197057857'
    url_test = f'{Urls.MS_URL_TEST}?year={YEAR}&quarter={QUARTER}'
    url_prod = f'{Urls.MS_URL_PROD}?year={YEAR}&quarter={QUARTER}'


class HeaderConstant:
    PASSPORT_TEXT = 'ПАСПОРТ'
    ZD_TEXT = 'ЗД'
    GR_TEXT = 'ГР'
    K_TEXT = 'К'
    STAFF_TEXT = 'ПЕРСОНАЛ'
    DEALERS_TEXT = 'ДИЛЕРЫ'
    USERS_TEXT = 'ПОЛЬЗОВАТЕЛИ'
    INDICATORS_TEXT = 'ПОКАЗАТЕЛИ'
    DOWNLOADS_TEXT = 'ЗАГРУЗКИ'
    EDITOR_TEXT = 'РЕДАКТОР'
    LOGS_TEXT = 'ЛОГИ'
    SELECT_DEALER_TEXT = 'ВЫБРАТЬ ДИЛЕРА'
    PKD_TEXT = 'ПКД'
    INTERRUPTION_TEXT = 'НАРУШЕНИЯ'
    NOTICES_TEXT = 'ОБЪЯВЛЕНИЯ'
    DOCUMENTS_TEXT = 'ДОКУМЕНТЫ'
    ACCOUNTING_TEXT = 'БУХГАЛТЕРИЯ'
    SRR_TEXT = 'SRR'
    REPORTS_TEXT = 'ОТЧЕТЫ'
    MENU_TEXT = ['ПАСПОРТ\nЗД\nГР\nК\nПЕРСОНАЛ\nДНМ\nДИЛЕРЫ\nПОЛЬЗОВАТЕЛИ\nПОКАЗАТЕЛИ\nЗАГРУЗКИ\nРЕДАКТОР\nЛОГИ']
    DEALER_NAME = 'АВА'
    LOADER_MSG = 'ЗАГРУЗКА...'


class MainConstant:
    ABOUT_BUTTONS = ['ИЗМЕНИТЬ\nКАМЕРЫ\nФОТО']


class Headers:
    HEADERS_ADMIN = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': f'token={Tokens.TOKEN}'
    }

    HEADERS_NO_CONTENT = {
        'accept': '*/*',
        'Cookie': f'token={Tokens.TOKEN}'
    }

    HEADERS_USER = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': f'token={Tokens.TOKEN_TEST}'
    }

    HEADERS_MY = {'authorization': f'Bearer {Tokens.MY_TOKEN}'}

    HEADERS_EXPORT = {
        'Authorization': f'Bearer {Tokens.TOKEN_EXPORT}'
    }

    HEADERS_USER_NEW = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': f'token={Tokens.MY_TOKEN}'
    }

    HEADERS_AN = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Tokens.TOKEN}'
    }


class StatusCodes:
    OK = 200
    CREATE = 201


class Assertions:
    STATUS = 'Неверный ответ сервера'
