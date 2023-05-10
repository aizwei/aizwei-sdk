from aizwei.connector.io_base import IOBase


class RunInput(IOBase):

    def validate_data(self, data) -> bool:
        if isinstance(data, dict):
            if not self.validate_data_row(data):
                return False
        else:
            return False
        return True
