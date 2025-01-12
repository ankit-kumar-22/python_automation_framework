import requests


class APIUtils:
    @staticmethod
    def get(endpoint, headers=None):
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response

    @staticmethod
    def post(endpoint, data, headers=None):
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
