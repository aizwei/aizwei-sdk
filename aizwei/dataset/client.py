import requests

from aizwei.client import AIZweiClient
from aizwei.dataset.dataset import Dataset


class Client(AIZweiClient):

    def create_dataset(self, dataset: Dataset) -> Dataset:
        api_response = self.api_call(path='/datasets', method='POST', request_body=dataset.to_api_request())
        return Dataset.from_api_response(api_response)

