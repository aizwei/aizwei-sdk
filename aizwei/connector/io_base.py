class IOBase:
    TYPE_STRING = 'string'
    TYPE_NUMBER = 'number'
    TYPE_ENUM = 'enum'
    TYPE_BOOLEAN = 'boolean'
    CONTEXT_TYPE_CONFIG = 'CONFIG'
    CONTEXT_TYPE_USER = 'USER'
    types = [TYPE_STRING, TYPE_NUMBER, TYPE_ENUM, TYPE_BOOLEAN]
    context_types = [CONTEXT_TYPE_CONFIG, CONTEXT_TYPE_USER]

    def __init__(self, schema: dict, data=None) -> None:
        if data is None:
            data = []
        self.schema = schema
        if not self.validate_schema(self.schema):
            self.throw_error('Invalid schema')
        self.data = data
        if not self.validate_data(self.data):
            self.throw_error('Invalid data')

    def validate_schema(self, schema: dict) -> bool:
        for name, var_schema in schema.items():
            if var_schema['type'] not in self.types:
                return False
            if var_schema['context_type'] not in self.context_types:
                return False
        return True

    def validate_data(self, data: list or dict) -> bool:
        if isinstance(data, list):
            for elem in data:
                if not isinstance(elem, dict):
                    return False
                if not self.validate_data_row(elem):
                    return False
        elif isinstance(data, dict):
            if not self.validate_data_row(data):
                return False
        else:
            return False
        return True

    def validate_data_row(self, data_item: dict) -> bool:
        for name, value in data_item.items():
            if self.schema[name]['type'] == self.TYPE_STRING and not isinstance(value, str):
                return False
            if self.schema[name]['type'] == self.TYPE_NUMBER and (
                    not isinstance(value, int) or not isinstance(value, float)):
                return False
            if self.schema[name]['type'] == self.TYPE_ENUM and not isinstance(value, str):
                return False
            if self.schema[name]['type'] == self.TYPE_BOOLEAN and not isinstance(value, bool):
                return False
        return True

    def throw_error(self, message: str):
        raise Exception(message)
