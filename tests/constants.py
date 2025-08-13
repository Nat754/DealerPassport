import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class Tokens:

    TOKEN = os.environ["PROD_ADMIN"]
    # TOKEN = os.environ["SEO_ADMIN"]
    # TOKEN = os.environ["TEST_ADMIN"]
    TOKEN_ADMIN = {'token': TOKEN}
    MS_PROD = {'Authorization': f'{os.environ["MS_PROD"]}'}
    MS_TEST = {'Authorization': f'{os.environ["MS_TEST"]}'}
    PKD = {'Authorization': f'{os.environ["AUTOCRM"]}'}
    REGISTRY = {'Authorization': f'{os.environ["REGISTRY"]}'}


class Urls:
    MAIN_URL = os.environ["MAIN_URL_PROD"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3001'
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3011'
    # MAIN_URL = os.environ["MAIN_URL_TEST"]
    MS_URL_TEST = os.environ["MS_URL_TEST"]
    MS_URL_PROD = os.environ["MS_URL_PROD"]
    CANDIDATES_URL = os.environ["CANDIDATES_URL"]
    REGISTRY_URL = os.environ["REGISTRY_URL"]

    AUTH = "/auth"
    PKD_URL = "/pkd/"
    PKD_INDICATORS_URL = "/pkd/indicators/"
    PKD_CHECKLISTS_URL = "/pkd/checklists/"
    INTERRUPTION_URL = "/violations/"
    NOTICES_URL = "/announcement/"
    DOCUMENTS_URL = "/documents/"
    ACCOUNTING_URL = "/accounting/"
    SRR_URL = "/srr/"
    REPORTS_URL = "/reports/"
    PASSPORT_BUTTON = MAIN_URL
    ZD_URL = "/zd/"
    GR_URL = "/gr/"
    Q_URL = "/q/"
    STAFF_URL = "/staff/"
    DEALERS_URL = "/dealers/"
    USERS_URL = "/users/"
    INDICATORS_URL = "/indicators/"
    UPLOADS_URL = "/uploads/"
    EDITOR_URL = "/editor/"
    LOGS_URL = "/logs/"
    EMAIL_LOGS_URL = "/logs/email"

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
                 MAIN_URL + PKD_INDICATORS_URL,
                 MAIN_URL + INTERRUPTION_URL,
                 MAIN_URL + NOTICES_URL]


class SRRConstant:
    # for prod
    LIST_GROUPS = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по периоду '
                   'продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение автомобилей '
                   'на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в динамике\nМашинозаезды по '
                   'дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты не обращавшиеся на гарантийный'
                   ' ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация ГИБДД\n1С УПП']
    # # for dev
    # LIST_GROUPS = ['Возвращение автомобилей на ТО по месяцу контроля\nВозвращение автомобилей на ТО по'
    #                ' периоду продаж\nВозвращение автомобилей на гарантийный ремонт по месяцу контроля\nВозвращение'
    #                ' автомобилей на гарантийный ремонт (свой-чужой) по месяцу контроля\nМашинозаезды в'
    #                ' динамике\nМашинозаезды по дилеру\nСреднесуточный пробег (семейство автомобиля-регион)\nКлиенты'
    #                ' не обращавшиеся на гарантийный ремонт\nSRR3\nSRR5\nПриглашение клиентов на ТО\nРегистрация'
    #                ' ГИБДД\nUVIN\nNS\n1С УПП']
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
                   'Справочник разделов фотогалереи', 'Справочник для выбора адреса', 'Справочник тарифов IVIDEON']
    # for dev
    # EDITOR_MENU = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения',
    #                'Виды нарушений', 'Редактор форм заявок-деклараций', 'Справочник должностей',
    #                'Каталог учебных программ', 'Справочники библиотеки документов', 'Редактор отчетов',
    #                'Справочник зон камер', 'Справочник информационных систем',
    #                'Справочник разделов фотогалереи', 'Шаблоны договоров', 'Справочник для выбора адреса',
    #                'Справочник доверенных лиц', 'Справочник тарифов IVIDEON']


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
    HEADERS = {
            'accept': '*/*',
            'Content-Type': 'application/json',
            'Cookie': f'token={Tokens.TOKEN}'
        }


class StatusCodes:
    OK = 200
    CREATE = 201


class Assertions:
    STATUS = 'Неверный ответ сервера'
