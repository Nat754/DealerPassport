import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class Urls:
    # MAIN_URL = os.environ["MAIN_URL_PROD"]
    MAIN_URL = os.environ["MAIN_URL_SEO"]
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3001'
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3011'
    # MAIN_URL = os.environ["MAIN_URL_SEO"] + ':3012'
    # MAIN_URL = os.environ["MAIN_URL_TEST"]
    MS_URL_TEST = os.environ["MS_URL_TEST"]
    MS_URL_PROD = os.environ["MS_URL_PROD"]
    CANDIDATES_URL = os.environ["CANDIDATES_URL"]
    CANDIDATES_TEST_URL = os.environ["CANDIDATES_TEST_URL"]
    REGISTRY_URL = os.environ["REGISTRY_URL"]
    AUTOCRM_URL = os.environ["AUTOCRM_URL"]

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
    TOKEN = os.environ["PROD_ADMIN"] if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] else os.environ["TEST_ADMIN"] \
        if Urls.MAIN_URL == os.environ["MAIN_URL_TEST"] else os.environ["SEO_ADMIN"]
    TOKEN_TEST = os.environ["SEO_TEST"]
    TOKEN_EXPORT = os.environ["EXPORT_API_PROD"] if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] \
        else os.environ["EXPORT_API_SEO"]
    TOKEN_EXPORT_NEW = os.environ["EXPORT_API_PROD_NEW"] if Urls.MAIN_URL == os.environ["MAIN_URL_PROD"] \
        else os.environ["NEW_EXPORT_SEO"]
    TOKEN_ADMIN = {'token': TOKEN}
    MS_PROD = {'Authorization': f'{os.environ["MS_PROD"]}'}
    MS_TEST = {'Authorization': f'{os.environ["MS_TEST"]}'}
    AUTOCRM = {'Authorization': f'{os.environ["AUTOCRM"]}'}
    REGISTRY = {'Authorization': f'{os.environ["REGISTRY"]}'}
    SA_SEO = os.environ["SA_SEO"]
    USER_NEW_SEO = os.environ["USER_NEW_SEO"]
    TOKEN_EXPORT_NEW_TEST = os.environ["EXPORT_API_TEST"]


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
    EDITOR_MENU = ['Глобальный рейтинг', 'Квартили', 'Персонал', 'База сотрудников', 'Подразделения', 'Виды нарушений',
                   'Редактор форм заявок-деклараций', 'Справочник должностей', 'Каталог учебных программ',
                   'Справочники библиотеки документов', 'Редактор отчетов', 'Справочник разделов фотогалереи',
                   'Шаблоны договоров', 'Справочник для выбора адреса','Справочник доверенных лиц',
                   'Справочник тарифов IVIDEON', 'Реквизиты АВТОВАЗ', 'Справочник показателей']


class IntegrationsConstants:
    YEAR = datetime.now().year
    QUARTER = datetime.now().month // 3
    MONTH = datetime.now().month
    DATE_NOW = datetime.now().date()
    DEALER_ID = '1197057857'
    MS_URL_TEST = Urls.MS_URL_TEST
    MS_URL_PROD = Urls.MS_URL_PROD

    invoices = [1335237260]
    str_dealers = """"""
    # print(str_dealers.replace('\n', ', '))

    dealers = [4152156182, 1737003781, 2645051184, 1274725624, 170829, 2499570285, 1200081385, 3285939517, 1686661281,
               1035505857, 6427883605, 3947393632, 6054737539, 1980576177, 1399584723, 2695350008, 2675022, 5060498914,
               5184981508, 1694396570, 1688245695, 699693303, 1413379286, 1415487020, 1576873737, 2709426520, 146686,
               2685777, 389904177, 5290934764, 1065912931, 1503305187, 1373228951, 3735900361, 3635948709, 146998,
               2873657568, 143873849, 170200480, 1522503850, 6538411911, 1313542596, 1290369427, 2635048, 1584615335,
               1163944746, 1705457368, 3930405934, 146776, 6348863, 1197057857, 1475456154, 2986910196, 3361287030,
               2646436, 4378444778, 6507365416, 1307431793, 1010174188, 1688258555, 1335237260, 1111284027, 154398894,
               2645183777, 1137632378, 2115743594, 1187941791, 4829079026, 4545156073, 3933830704, 2668130, 2992869580,
               1445609573, 1298272463, 147031, 147413, 3634235482, 1065913328, 2646327, 152316288, 3452705459, 147268,
               4831856410, 85111403, 1737618295, 1229495508, 2906388822, 1042807335, 1177844714, 1972159203, 683104877,
               1463794573, 966995950, 1415517319, 1400386782, 614379713, 1532081231, 600794570, 147288, 708120633,
               1526936197, 1335723999, 1481485684, 117900776, 3634188644, 6339801716, 2713480944, 6336352401,
               3452721029, 109580422, 131996579, 3634279528, 1380790938, 2709423821, 1446093945, 146602, 1980577412,
               5134416904, 2816414831, 1711777704, 51425454, 5263772000, 1817322284, 3240321, 114184902, 1723584942,
               5134284793, 49643734, 3452722716, 1736466549, 6339739797, 1546572934, 1010174300, 1193537702, 6339763108,
               467221581, 1192211249, 4112151322, 3853657890, 2794108, 295722, 2708802, 699694766, 1567342250,
               1316818999, 4736485398, 124659097, 1526938630, 1234651878, 4267115913, 2715675712, 44954283, 103098426,
               2397095347, 4866413121, 1686661040, 166212973, 1187686392, 1220410407, 2625432, 4736486222, 3943117523,
               111726946, 2875197666, 1733458027, 2785800109, 5060498629, 4210151707, 3634253345, 1526940282,
               1796633966, 315326, 2937949679, 119345065, 139066020, 1185335155, 1765131850, 5694758588, 2846660092,
               261632, 1451754861, 4819058122, 293424768, 2778107370, 3630475564, 128928036, 6701055171, 1733462122,
               1789111767, 941106659, 1139617102, 2709428185, 6228280085, 1089977232, 2632144231, 1365297204, 2802683,
               4039117087, 4950876784, 1528107732, 47578027, 5694759248, 1042806056, 1076577625, 1236080712,
               6538411736, 120934304, 3963319897, 3935274086, 707311111, 2616039, 1206426015, 129911977, 1223128445,
               146713, 2968496422, 1694396940, 1240786295, 1268384101, 3849746, 699697605, 1278911929, 985153266,
               3729355169, 1395601186, 146830708, 3634193037, 4014587642, 2042778208, 1174437313, 978309020,
               1089977628, 3452707750, 5423365453, 2665648, 3634279402]
    print(len(dealers))
    appeals = []


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

    HEADERS_SA_SEO = {'accept': '*/*',
                      'Content-Type': 'application/json',
                      'Cookie': f'token={Tokens.SA_SEO}'
                      }

    HEADERS_EXPORT = {
        'Authorization': f'Bearer {Tokens.TOKEN_EXPORT}'
    }

    HEADERS_EXPORT_NEW = {
        'Authorization': f'Bearer {Tokens.TOKEN_EXPORT_NEW}'
    }

    HEADERS_EXPORT_NEW_TEST = {
        'Authorization': f'{Tokens.TOKEN_EXPORT_NEW_TEST}'
    }

    HEADERS_USER_NEW_SEO = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': f'token={Tokens.USER_NEW_SEO}'
    }

    HEADERS_AN = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Tokens.TOKEN}'
    }


class StatusCodes:
    OK = 200
    CREATE = 201
