from aizwei.client import AIZweiClient
from aizwei.dataset.data_batch import DataBatch
from aizwei.dataset.dataset import Dataset


class Client(AIZweiClient):

    def create_dataset(self, dataset: Dataset) -> Dataset:
        api_response = self.api_call(path='/datasets', method='POST', request_body=dataset.to_api_request())
        return Dataset.from_api_response(api_response)

    def get_dataset(self, dataset_id: str) -> Dataset:
        api_response = self.api_call(path=f'/datasets/{dataset_id}', method='GET')
        return Dataset.from_api_response(api_response)

    def remove_dataset(self, dataset_id: str):
        self.api_call(path=f'/datasets/remove/{dataset_id}', method='GET')

    def push_data(self, data_batch: DataBatch):
        self.api_call(path=f'/datasets/{data_batch.dataset.id}/data', method='POST', request_body=data_batch.to_api_request())
