import requests


class RESTApi:

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return requests.get(url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return requests.post(url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return requests.put(url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return requests.delete(url=url, headers=headers, data=data, cookies=cookies)
