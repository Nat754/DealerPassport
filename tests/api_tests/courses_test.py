import allure
import pytest
# import json
# from pprint import pprint
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions


@allure.epic('CoursesTest')
@pytest.mark.manual_run
class TestApi:
    url = Urls
    token = Tokens
    page = RESTApi()
    header = Headers
    const = IntegrationsConstants
    code = StatusCodes


@allure.suite('Courses')
@pytest.mark.manual_run
class TestCourses(TestApi):
    @allure.suite('EmployeeCourses')
    @pytest.mark.manual_run
    class TestEmployeeCourses(TestApi):

        @pytest.mark.auto_test
        @allure.title('Получить Курс')
        def test_get_employee_courses(self):
            url = f'{self.url.MAIN_URL}/internal-api/employee/courses?actualOn={self.const.DATE_NOW}&page=0&count=2'
                   # f'&code=%D1%80%D0%BE%D0%BF&codeIS=5552&name=%D1%80%D0%BE%D0%BF&levelId=2&searchText=%D1%80%D0%BE'
                   # f'%D0%B7%D1%87&sortField=code&sortType=ASC'
            headers = self.header.HEADERS_ADMIN
            response = self.page.get(url=url, headers=headers)
            # print(response.status_code)
            # pprint(response.json())
            Assertions.assert_status_code(response, self.code.OK)

        @pytest.mark.auto_test
        @allure.title('Получить Курс по ид')
        def test_get_employee_course_by_id(self):
            url = f'{self.url.MAIN_URL}/internal-api/employee/courses/235'
            headers = self.header.HEADERS_ADMIN
            response = self.page.get(url=url, headers=headers)
            # print(response.status_code)
            # pprint(response.json())
            Assertions.assert_status_code(response, self.code.OK)

        # @allure.title('Создать Курс')
        # def test_post_employee_courses(self):
        #     url = f'{self.url.MAIN_URL}/internal-api/employee/courses'
        #     headers = self.header.HEADERS_ADMIN
        #     payload = json.dumps({
        #         "code": "БК92",
        #         "name": "БК92 Принципы92 деловой92 коммуникации92",
        #         "status": "active",
        #         "certificateValidityPeriod": 0,
        #         "codeIS": "9992",
        #         'levelId': 2
        #     })
        #     response = self.page.post(url=url, headers=headers, data=payload)
        #     print(response.status_code)
        #     print(response.json())
        #
        # @allure.title('Изменить Курс')
        # def test_put_employee_courses(self):
        #     url = f'{self.url.MAIN_URL}/internal-api/employee/courses'
        #     headers = self.header.HEADERS_ADMIN
        #     payload = json.dumps({
        #         "code": "5551",
        #         'levelId': 2,
        #         "instanceId": 233,
        #         "replacementCourseIds": [38, 46, 74, 12, 3, 90]
        #     })
        #     response = self.page.put(url=url, headers=headers, data=payload)
        #     print(response.status_code)
        #     pprint(response.json())
