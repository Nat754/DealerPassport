import requests


class MSPortal:

    @staticmethod
    def get_quality(url, headers):
        return requests.request("GET", url, headers=headers)
