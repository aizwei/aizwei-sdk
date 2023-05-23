# Unit Test for dataset.client.Client class

import unittest
from unittest.mock import patch

from aizwei.dataset.client import Client
from aizwei.dataset.dataset import Dataset
from aizwei.dataset.schema import Schema


class TestClient(unittest.TestCase):


    def setUp(self) -> None:
        self.client = Client(auth_token='test_token')
        self.dataset = Dataset(name='test_dataset', description='test_description', schema=Schema())

    @patch('aizwei.dataset.client.Client.api_call')
    def test_get_dataset(self, mock_get):
        mock_get.return_value = {
            'id': 'test_id',
            'name': 'test_dataset',
            'description': 'test_description',
            'schema': [
                {
                    'name': 'field_number',
                    'type': 'integer'
                },
                {
                    'name': 'field_string',
                    'type': 'string'
                },
                {
                    'name': 'field_boolean',
                    'type': 'boolean'
                }
            ]
        }
        dataset = self.client.get_dataset('test_dataset')
        self.assertEqual('test_id', dataset.id)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(3, dataset.schema.get_field_count())
        self.assertEqual('field_number', dataset.schema.get_field_names()[0])
        self.assertEqual('field_string', dataset.schema.get_field_names()[1])
        self.assertEqual('field_boolean', dataset.schema.get_field_names()[2])
        self.assertEqual(Schema.TYPE_INTEGER, dataset.schema.get_field_type('field_number'))
        self.assertEqual(Schema.TYPE_STRING, dataset.schema.get_field_type('field_string'))
        self.assertEqual(Schema.TYPE_BOOLEAN, dataset.schema.get_field_type('field_boolean'))

    @patch('aizwei.dataset.client.Client.api_call')
    def test_create_dataset(self, mock_api_call):
        mock_api_call.return_value = {
            'id': 'test_id',
            'name': 'test_dataset',
            'description': 'test_description',
            'schema': [
                {
                    'name': 'field_number',
                    'type': 'integer'
                },
                {
                    'name': 'field_string',
                    'type': 'string'
                },
                {
                    'name': 'field_boolean',
                    'type': 'boolean'
                }
            ]
        }
        dataset = self.client.create_dataset(self.dataset)
        self.assertEqual('test_id', dataset.id)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(3, dataset.schema.get_field_count())
        self.assertEqual('field_number', dataset.schema.get_field_names()[0])
        self.assertEqual('field_string', dataset.schema.get_field_names()[1])
        self.assertEqual('field_boolean', dataset.schema.get_field_names()[2])
        self.assertEqual(Schema.TYPE_INTEGER, dataset.schema.get_field_type('field_number'))
        self.assertEqual(Schema.TYPE_STRING, dataset.schema.get_field_type('field_string'))
        self.assertEqual(Schema.TYPE_BOOLEAN, dataset.schema.get_field_type('field_boolean'))

