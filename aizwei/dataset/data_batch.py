from aizwei.dataset.dataset import Dataset


class DataBatch:
    def __init__(self, data: list, dataset: Dataset):
        self.data = data
        self.dataset = dataset
        self.dataset.schema.validate_data_list_schema(data)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def to_dict(self) -> dict:
        return {
            'data': self.data,
            'dataset': self.dataset.to_dict()
        }

    def to_api_request(self) -> list:
        return self.data

    @classmethod
    def from_dict(cls, data_batch_dict: dict) -> 'DataBatch':
        return cls(
            data=data_batch_dict['data'],
            dataset=Dataset.from_dict(data_batch_dict['dataset'])
        )
