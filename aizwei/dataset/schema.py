
class Schema:
    TYPE_STRING = 'string'
    TYPE_INTEGER = 'integer'
    TYPE_FLOAT = 'float'
    TYPE_BOOLEAN = 'boolean'

    def __init__(self) -> None:
        self.fields = []

    def add_field(self, name: str, type: str):
        if type not in [self.TYPE_STRING, self.TYPE_INTEGER, self.TYPE_FLOAT, self.TYPE_BOOLEAN]:
            raise Exception('Invalid field type')
        # Raise exception if field name already exists
        for field in self.fields:
            if field['name'] == name:
                raise Exception('Field name already exists')
        self.fields.append({
            'name': name,
            'type': type
        })

    def get_fields(self) -> list:
        return self.fields

    def get_field(self, name) -> dict or None:
        for field in self.fields:
            if field['name'] == name:
                return field
        return None

    def get_field_names(self) -> list:
        return [field['name'] for field in self.fields]

    def get_field_types(self) -> list:
        return [field['type'] for field in self.fields]

    def get_field_type(self, name) -> str or None:
        for field in self.fields:
            if field['name'] == name:
                return field['type']
        return None

    def get_field_index(self, name) -> int or None:
        for i, field in enumerate(self.fields):
            if field['name'] == name:
                return i
        return None

    def get_field_count(self) -> int:
        return len(self.fields)

    def to_dict(self) -> dict:
        return {field['name']: field['type'] for field in self.fields}

    def to_api_request(self) -> list:
        return [{'name': field['name'], 'type': field['type']} for field in self.fields]

    @classmethod
    def from_dict(cls, schema_dict: dict) -> 'Schema':
        schema = cls()
        for name, type in schema_dict.items():
            schema.add_field(name, type)
        return schema

    @classmethod
    def from_api_response(cls, api_response: list) -> 'Schema':
        schema = cls()
        for field in api_response:
            schema.add_field(field['name'], field['type'])
        return schema
