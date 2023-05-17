# System test for aizwei.dataset.client.Client class

from unittest import TestCase
from unittest.mock import patch

from aizwei.dataset.client import Client
from aizwei.dataset.dataset import Dataset
from aizwei.dataset.schema import Schema


class TestClient(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        schema = Schema()
        schema.add_field('field_number', Schema.TYPE_INTEGER)
        schema.add_field('field_string', Schema.TYPE_STRING)
        schema.add_field('field_float', Schema.TYPE_FLOAT)
        self.dataset = Dataset(name='test_dataset', description='test_description', schema=schema)

    def test_create_get_remove_dataset(self):

        # Create dataset
        dataset = self.client.create_dataset(self.dataset)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(3, dataset.schema.get_field_count())
        self.assertEqual('field_number', dataset.schema.get_field_names()[0])
        self.assertEqual('field_string', dataset.schema.get_field_names()[1])
        self.assertEqual('field_float', dataset.schema.get_field_names()[2])
        self.assertEqual(Schema.TYPE_INTEGER, dataset.schema.get_field_type('field_number'))
        self.assertEqual(Schema.TYPE_STRING, dataset.schema.get_field_type('field_string'))
        self.assertEqual(Schema.TYPE_FLOAT, dataset.schema.get_field_type('field_float'))

        # Get dataset
        dataset = self.client.get_dataset(dataset.id)
        self.assertEqual('test_dataset', dataset.name)
        self.assertEqual('test_description', dataset.description)
        self.assertEqual(3, dataset.schema.get_field_count())
        self.assertEqual('field_number', dataset.schema.get_field_names()[0])
        self.assertEqual('field_string', dataset.schema.get_field_names()[1])
        self.assertEqual('field_float', dataset.schema.get_field_names()[2])
        self.assertEqual(Schema.TYPE_INTEGER, dataset.schema.get_field_type('field_number'))
        self.assertEqual(Schema.TYPE_STRING, dataset.schema.get_field_type('field_string'))
        self.assertEqual(Schema.TYPE_FLOAT, dataset.schema.get_field_type('field_float'))

        # Remove dataset
        self.client.remove_dataset(dataset.id)
        with self.assertRaises(Exception):
            self.client.get_dataset(dataset.id)

