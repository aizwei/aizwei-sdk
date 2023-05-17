
class Schema:
    TYPE_STRING = 'string'
    TYPE_INTEGER = 'integer'
    TYPE_FLOAT = 'float'
    TYPE_BOOLEAN = 'boolean'

    def __init__(self) -> None:
        self.fields = []

    def add_field(self, name: str, type: str):
        # Raise exception if field name already exists
        if self.field_exists(name):
            raise Exception('Field name already exists')
        if not self.is_valid_field_type(type):
            raise Exception('Invalid field type')
        self.fields.append({
            'name': name,
            'type': type
        })

    def is_valid_field_type(self, type: str) -> bool:
        return type in [self.TYPE_STRING, self.TYPE_INTEGER, self.TYPE_FLOAT, self.TYPE_BOOLEAN]

    def field_exists(self, name: str) -> bool:
        for field in self.fields:
            if field['name'] == name:
                return True
        return False

    def validate_data_schema(self, data: dict) -> bool:
        for field in self.fields:
            if field['name'] not in data:
                return False
            if not self.validate_data_type(field['name'], data[field['name']]):
                return False

        return True

    def validate_data_list_schema(self, data: list) -> bool:
        for row in data:
            if not self.validate_data_schema(row):
                return False
        return True

    def validate_data_type(self, name: str, value) -> bool:
        for field in self.fields:
            if field['name'] == name:
                if field['type'] == self.TYPE_STRING:
                    return isinstance(value, str)
                elif field['type'] == self.TYPE_INTEGER:
                    return isinstance(value, int)
                elif field['type'] == self.TYPE_FLOAT:
                    return isinstance(value, float)
                elif field['type'] == self.TYPE_BOOLEAN:
                    return isinstance(value, bool)
        return False

    def remove_field(self, name: str):
        for i, field in enumerate(self.fields):
            if field['name'] == name:
                self.fields.pop(i)
                return
        raise Exception('Field name does not exist')

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
