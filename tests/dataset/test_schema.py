# Unit test for Schema class
import unittest

from aizwei.dataset import Schema


class TestSchema(unittest.TestCase):

    def setUp(self) -> None:
        self.schema = Schema()
        self.schema.add_field(name='field_number', type=Schema.TYPE_NUMBER)
        self.schema.add_field(name='field_string', type=Schema.TYPE_STRING)
        self.schema.add_field(name='field_boolean', type=Schema.TYPE_BOOLEAN)

    def test_create(self):
        self.assertEqual(3, self.schema.get_field_count())
        self.assertEqual('field_number', self.schema.get_field_names()[0])
        self.assertEqual('field_string', self.schema.get_field_names()[1])
        self.assertEqual('field_boolean', self.schema.get_field_names()[2])
        self.assertEqual('number', self.schema.get_field_type('field_number'))
        self.assertEqual('string', self.schema.get_field_type('field_string'))
        self.assertEqual('boolean', self.schema.get_field_type('field_boolean'))

    def test_to_dict(self):
        schema_dict = self.schema.to_dict()
        self.assertEqual(3, len(schema_dict))
        self.assertEqual('number', schema_dict['field_number'])
        self.assertEqual('string', schema_dict['field_string'])
        self.assertEqual('boolean', schema_dict['field_boolean'])

    def test_to_api_request(self):
        schema_dict = self.schema.to_api_request()
        self.assertEqual(3, len(schema_dict))
        self.assertEqual('number', schema_dict[0]['type'])
        self.assertEqual('string', schema_dict[1]['type'])
        self.assertEqual('boolean', schema_dict[2]['type'])
        self.assertEqual('field_number', schema_dict[0]['name'])
        self.assertEqual('field_string', schema_dict[1]['name'])
        self.assertEqual('field_boolean', schema_dict[2]['name'])

    def test_from_dict(self):
        schema_dict = {
            'field_number': 'number',
            'field_string': 'string',
            'field_boolean': 'boolean'
        }
        schema = Schema.from_dict(schema_dict)
        self.assertEqual(3, schema.get_field_count())
        self.assertEqual('field_number', schema.get_field_names()[0])
        self.assertEqual('field_string', schema.get_field_names()[1])
        self.assertEqual('field_boolean', schema.get_field_names()[2])
        self.assertEqual('number', schema.get_field_type('field_number'))
        self.assertEqual('string', schema.get_field_type('field_string'))
        self.assertEqual('boolean', schema.get_field_type('field_boolean'))

    def test_from_dict_invalid_type(self):
        schema_dict = {
            'field_number': 'number',
            'field_string': 'string',
            'field_boolean': 'invalid'
        }
        with self.assertRaises(Exception):
            Schema.from_dict(schema_dict)

    def test_get_field_index(self):
        self.assertEqual(0, self.schema.get_field_index('field_number'))
        self.assertEqual(1, self.schema.get_field_index('field_string'))
        self.assertEqual(2, self.schema.get_field_index('field_boolean'))

    def test_get_field_index_not_found(self):
        self.assertIsNone(self.schema.get_field_index('not_found'))

    def test_get_field(self):
        field = self.schema.get_field('field_number')
        self.assertEqual('field_number', field['name'])
        self.assertEqual('number', field['type'])

    def test_get_field_not_found(self):
        self.assertIsNone(self.schema.get_field('not_found'))

    def test_get_field_type(self):
        self.assertEqual('number', self.schema.get_field_type('field_number'))
        self.assertEqual('string', self.schema.get_field_type('field_string'))
        self.assertEqual('boolean', self.schema.get_field_type('field_boolean'))

    def test_get_field_type_not_found(self):
        self.assertIsNone(self.schema.get_field_type('not_found'))

    def test_get_field_names(self):
        self.assertEqual(3, len(self.schema.get_field_names()))
        self.assertEqual('field_number', self.schema.get_field_names()[0])
        self.assertEqual('field_string', self.schema.get_field_names()[1])
        self.assertEqual('field_boolean', self.schema.get_field_names()[2])

    def test_get_field_count(self):
        self.assertEqual(3, self.schema.get_field_count())

    def test_add_field(self):
        self.schema.add_field(name='field_new', type=Schema.TYPE_NUMBER)
        self.assertEqual(4, self.schema.get_field_count())
        self.assertEqual('field_new', self.schema.get_field_names()[3])
        self.assertEqual('number', self.schema.get_field_type('field_new'))

    def test_add_field_invalid_type(self):
        with self.assertRaises(Exception):
            self.schema.add_field(name='field_new', type='invalid')

    def test_add_field_duplicate(self):
        with self.assertRaises(Exception):
            self.schema.add_field(name='field_number', type=Schema.TYPE_NUMBER)
