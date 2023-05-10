from aizwei.dataset import Schema


class Dataset:
    def __init__(self, name: str, description: str, schema: Schema):
        self.name = name
        self.description = description
        self.schema = schema

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'schema': self.schema.to_dict()
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
            name=dataset_dict['name'],
            description=dataset_dict['description'],
            schema=Schema.from_dict(dataset_dict['schema'])
        )

    @classmethod
    def from_api_response(cls, api_response) -> 'Dataset':
        return cls(
            name=api_response['name'],
            description=api_response['description'],
            schema=Schema.from_api_response(api_response['schema'])
        )


