from aizwei.dataset import Schema


class Dataset:
    def __init__(self, name: str, description: str, schema: Schema, id: str = None):
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.schema: Schema = schema

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
        if 'id' in api_response:
            dataset = cls(
                name=api_response['name'],
                description=api_response['description'],
                schema=Schema.from_api_response(api_response['schema']),
                id=api_response['id']
            )
            return dataset

        dataset = cls(
            name=api_response['name'],
            description=api_response['description'],
            schema=Schema.from_api_response(api_response['schema'])
        )
        return dataset


