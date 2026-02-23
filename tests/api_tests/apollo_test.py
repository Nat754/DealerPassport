import pytest
import json
from pages.rest_api_methods import RESTApi
from tests.constants import Urls, Tokens, Headers, IntegrationsConstants, StatusCodes
from pages.assertions import Assertions


class TestGQL:
    token = Tokens
    header = Headers
    url = Urls
    page = RESTApi()
    const = IntegrationsConstants
    code = StatusCodes

    @pytest.mark.manual_test
    def test_gql(self):
        url = f"{self.url.MAIN_URL}/graphql"
        payload = json.dumps({
            "operationName": "GetDealer",
            "variables": {
                "dealerId": "1197057857"
                },
            "query": "query GetDealer($dealerId: ID!) {DealerGetter {getDealer(DealerId: $dealerId){id}}}"
        })
        headers = self.token.TOKEN_ADMIN | self.header.HEADERS_ADMIN
        response = self.page.post(url, headers=headers, data=payload)
        # print(response.json())
        Assertions.assert_status_code(response, self.code.OK)
