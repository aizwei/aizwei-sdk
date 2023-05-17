import os

import requests


class AIZweiClient:

    def __init__(self, auth_token: str = None, base_url: str = None) -> None:
        if auth_token is None:
            # Get auth token from environment variable
            auth_token = os.environ.get('AIZWEI_AUTH_TOKEN')
            if auth_token is None:
                raise Exception("AIZWEI_AUTH_TOKEN environment variable is not set")
        if base_url is None:
            # Get base url from environment variable
            base_url = os.environ.get('AIZWEI_API_BASE_URL')
            if base_url is None:
                base_url = 'https://www.aizwei.co/prod/expose'
        self.auth_token = auth_token
        self.base_url = base_url

    def get_headers(self) -> dict:

        return {
            'Authorization': f'Bearer {self.auth_token}'
        }

    def api_call(self, path: str, method: str, request_body: dict or list = None) -> dict or list or None:
        request_url = f"{self.base_url}{path}"
        headers = self.get_headers()
        request = requests.request(method, request_url, json=request_body, headers=headers)
        if request.status_code == 200 or request.status_code == 201:
            # Check request empty
            if request.text == '':
                return None
            return request.json()
        else:
            raise Exception(f"Error calling API {request_url} {request}")

