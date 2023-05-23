from aizwei.dataset import Schema


class Dataset:
    def __init__(self, name: str, description: str, schema: Schema, id: str = None, dataset_url: str = None):
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.schema: Schema = schema
        self.dataset_url: str = dataset_url

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'schema': self.schema.to_dict(),
            'datasetUrl': self.dataset_url,
        }

    def to_api_request(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'schema': self.schema.to_api_request()
        }

    @classmethod
    def from_dict(cls, dataset_dict: dict) -> 'Dataset':
        return cls(
            id=dataset_dict['id'] if 'id' in dataset_dict else None,
            dataset_url=dataset_dict['datasetUrl'] if 'datasetUrl' in dataset_dict else None,
            name=dataset_dict['name'],
            description=dataset_dict['description'],
            schema=Schema.from_dict(dataset_dict['schema'])
        )

    @classmethod
    def from_api_response(cls, api_response) -> 'Dataset':
        dataset = cls(
            name=api_response['name'],
            description=api_response['description'],
            schema=Schema.from_api_response(api_response['schema']),
            id=api_response['id'] if 'id' in api_response else None,
            dataset_url=api_response['datasetUrl'] if 'datasetUrl' in api_response else None
        )
        return dataset


