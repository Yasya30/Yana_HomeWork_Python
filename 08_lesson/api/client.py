import os
import requests
from dotenv import load_dotenv

load_dotenv()


class YougileClient:
    """Базовый клиент для работы с API Yougile"""

    def __init__(self):
        self.base_url = os.getenv("YOUILE_API_URL", "https://api.yougile.com")
        self.token = os.getenv("YOUILE_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _request(self, method, endpoint, data=None):
        """Универсальный метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method, url=url, json=data, headers=self.headers
        )
        return response

    def post(self, endpoint, data):
        """POST запрос"""
        return self._request("POST", endpoint, data)

    def put(self, endpoint, data):
        """PUT запрос"""
        return self._request("PUT", endpoint, data)

    def get(self, endpoint):
        """GET запрос"""
        return self._request("GET", endpoint)
    