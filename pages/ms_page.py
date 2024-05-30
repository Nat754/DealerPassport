import requests
from dotenv import load_dotenv

load_dotenv()


class MSPortal:

    @staticmethod
    def get_quality(url, headers):
        return requests.request("GET", url, headers=headers)
