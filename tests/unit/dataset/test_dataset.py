# Unit test for Dataset class
import unittest

from aizwei.dataset import Dataset, Schema


class TestDataset(unittest.TestCase):

    def setUp(self) -> None:
        self.schema = Schema()
        self.schema.add_field(name='field_number', type=Schema.TYPE_INTEGER)
        self.schema.add_field(name='field_string', type=Schema.TYPE_STRING)
        self.schema.add_field(name='field_boolean', type=Schema.TYPE_BOOLEAN)
        self.dataset = Dataset(name='test_dataset', description='test_description', schema=self.schema)

    def test_create(self):
        self.assertEqual('test_dataset', self.dataset.name)
        self.assertEqual('test_description', self.dataset.description)
        self.assertEqual(3, self.dataset.schema.get_field_count())
        self.assertEqual('field_number', self.dataset.schema.get_field_names()[0])
        self.assertEqual('field_string', self.dataset.schema.get_field_names()[1])
        self.assertEqual('field_boolean', self.dataset.schema.get_field_names()[2])
        self.assertEqual(Schema.TYPE_INTEGER, self.dataset.schema.get_field_type('field_number'))
        self.assertEqual(Schema.TYPE_STRING, self.dataset.schema.get_field_type('field_string'))
        self.assertEqual(Schema.TYPE_BOOLEAN, self.dataset.schema.get_field_type('field_boolean'))

    def test_to_dict(self):
        dataset_dict = self.dataset.to_dict()
        self.assertEqual('test_dataset', dataset_dict['name'])
        self.assertEqual('test_description', dataset_dict['description'])
        self.assertEqual(3, len(dataset_dict['schema']))
        self.assertEqual(Schema.TYPE_INTEGER, dataset_dict['schema']['field_number'])
        self.assertEqual(Schema.TYPE_STRING, dataset_dict['schema']['field_string'])
        self.assertEqual(Schema.TYPE_BOOLEAN, dataset_dict['schema']['field_boolean'])

    def test_to_api_request(self):
        dataset_dict = self.dataset.to_api_request()
        self.assertEqual('test_dataset', dataset_dict['name'])
        self.assertEqual('test_description', dataset_dict['description'])
        self.assertEqual(3, len(dataset_dict['schema']))
        self.assertEqual(Schema.TYPE_INTEGER, dataset_dict['schema'][0]['type'])
        self.assertEqual(Schema.TYPE_STRING, dataset_dict['schema'][1]['type'])
        self.assertEqual(Schema.TYPE_BOOLEAN, dataset_dict['schema'][2]['type'])


    def test_from_dict(self):
        dataset_dict = {
            'name': 'test_dataset',
            'description': 'test_description',
            'schema': {
                'field_number': 'integer',
                'field_string': 'string',
                'field_boolean': 'boolean'
            }
        }
        dataset = Dataset.from_dict(dataset_dict)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(self.schema.to_dict(), dataset.schema.to_dict())

    def test_from_api_response(self):
        api_response = {
            'name': 'test_dataset',
            'description': 'test_description',
            'schema': [{'name': 'field_number', 'type': 'integer'},
                       {'name': 'field_string', 'type': 'string'},
                       {'name': 'field_boolean', 'type': 'boolean'}]
        }
        dataset = Dataset.from_api_response(api_response)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(self.schema.to_api_request(), dataset.schema.to_api_request())
