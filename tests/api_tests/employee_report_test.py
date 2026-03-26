import allure
import pytest
import json
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions
from datetime import datetime


@allure.epic('EducationProgramsTest')
class TestApi:
    url = Urls
    token = Tokens
    page = RESTApi()
    header = Headers
    const = IntegrationsConstants
    code = StatusCodes


@allure.suite('EducationPrograms')
@pytest.mark.manual_run
class TestEducationPrograms(TestApi):

    @allure.title('Таблица с обученностью по курсам')
    def test_get_report_courses(self):
        url = (f'{self.url.MAIN_URL}/internal-api/employee/statistics/report/courses?dealerGroup[ids]['
               f'0]=1197057857&group=id&actualOn={datetime.now().date()}')
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Таблица с обученностью по курсу')
    def test_get_report_course(self):
        url = (f'{self.url.MAIN_URL}/internal-api/employee/statistics/report/courses?dealerGroup[ids]['
               f'0]=1197057857&group=id&actualOn={datetime.now().date()}')
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)

    @pytest.mark.skip
    @allure.title('Создать новую учебную программу')
    def test_post_education_programs(self):
        url = f'{self.url.MAIN_URL}/internal-api/employee/education-programs'
        headers = self.header.HEADERS_ADMIN
        payload = json.dumps({
            "positionIds": [232],
            "levels": []
        })
        response = self.page.post(url=url, headers=headers, data=payload)
        Assertions.assert_status_code(response, self.code.CREATE)

    @pytest.mark.skip
    @allure.title('Изменить условия учебной программы')
    def test_put_education_programs(self):
        url = f'{self.url.MAIN_URL}/internal-api/employee/education-programs'
        headers = self.header.HEADERS_ADMIN
        payload = json.dumps({
            "instanceId": 18,
            "positionIds": [237],
            "levels": [
                {
                    "levelId": 1,
                    "courseIds": [237]
                },
                {
                    "levelId": 3,
                    "courseIds": [19]
                }
            ]
        })
        response = self.page.put(url=url, headers=headers, data=payload)
        Assertions.assert_status_code(response, self.code.CREATE)

    @pytest.mark.skip
    @allure.title('Деактивировать учебную программу')
    def test_delete_education_programs(self):
        url = f'{self.url.MAIN_URL}/internal-api/employee/education-programs'
        headers = self.header.HEADERS_ADMIN
        payload = json.dumps({"instanceId": 17})
        response = self.page.delete(url=url, headers=headers, data=payload)
        Assertions.assert_status_code(response, self.code.OK)

    @allure.title('Получить учебную программу с курсами и уровнями')
    def test_get_education_programs_by_id(self):
        url = f'{self.url.MAIN_URL}/internal-api/employee/education-programs/18?actualOn={datetime.now().date()}'
        headers = self.header.HEADERS_ADMIN
        response = self.page.get(url, headers=headers)
        Assertions.assert_status_code(response, self.code.OK)
