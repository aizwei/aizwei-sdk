import os

import requests


class AIZweiClient:

    def __init__(self, auth_token: str = None, base_url: str = 'https://www.aizwei.co/prod/expose') -> None:
        if auth_token is None:
            # Get auth token from environment variable
            auth_token = os.environ.get('AIZWEI_AUTH_TOKEN')
            if auth_token is None:
                raise Exception("AIZWEI_AUTH_TOKEN environment variable is not set")

        self.auth_token = auth_token
        self.base_url = base_url

    def get_headers(self) -> dict:

        return {
            'Authorization': f'Bearer {self.auth_token}'
        }

    def api_call(self, path: str, method: str, request_body: dict = None) -> dict:
        request_url = f"{self.base_url}{path}"
        headers = self.get_headers()
        request = requests.request(method, request_url, json=request_body, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception(f"Error calling API {request_url} {request}")

