import unittest
from pilifana.conversion.structure import Flattener


class FlattenerTest(unittest.TestCase):
    def test_flattening_primitive_integers(self):
        source = 1
        expected = {'prefix': source}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_primitive_strings(self):
        source = 'hello'
        expected = {'prefix': source}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_primitive_true(self):
        source = True
        expected = {'prefix': source}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_primitive_false(self):
        source = False
        expected = {'prefix': source}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_primitive_double(self):
        source = 13.37
        expected = {'prefix': source}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_dictionary_one_level(self):
        source = {'item1': 1, 'item2': 'Hello', 'item3': 12.36}
        expected = source

        flattener = Flattener()

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_dictionary_multi_level(self):
        source = {
                'item1': {'subitem1': 2, 'subitem2': {'subsubitem1': True}},
                'item2': 'Hello',
                'item3': 12.36
            }

        expected = {
            'item1.subitem1': 2,
            'item1.subitem2.subsubitem1': True,
            'item2': 'Hello',
            'item3': 12.36
        }

        flattener = Flattener()

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_dictionary_multi_level_with_prefix(self):
        source = {
            'item1': {'subitem1': 2, 'subitem2': {'subsubitem1': True}},
            'item2': 'Hello',
            'item3': 12.36
        }

        expected = {
            'prefix.item1.subitem1': 2,
            'prefix.item1.subitem2.subsubitem1': True,
            'prefix.item2': 'Hello',
            'prefix.item3': 12.36
        }

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_list_simple(self):
        source = [1, 2, True, 'foo']
        expected = {'[0]': 1, '[1]': 2, '[2]': True, '[3]': 'foo'}

        flattener = Flattener()

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_list_simple_with_prefix(self):
        source = [1, 2, True, 'foo']
        expected = {'prefix[0]': 1, 'prefix[1]': 2, 'prefix[2]': True, 'prefix[3]': 'foo'}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_list_multidimensional(self):
        source = [1, 2, ['foo', 'bar', 'baz'], 3]
        expected = {
                    'prefix[0]': 1, 
                    'prefix[1]': 2, 
                    'prefix[2][0]': 'foo', 
                    'prefix[2][1]': 'bar',
                    'prefix[2][2]': 'baz',
                    'prefix[3]': 3}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_list_with_dict(self):
        source = [{'foo': 1, 'bar': 2}, {'foo': 3, 'bar': 4, 'baz': 5}, 'test']
        expected = {
            'prefix[0].foo': 1,
            'prefix[0].bar': 2,
            'prefix[1].foo': 3,
            'prefix[1].bar': 4,
            'prefix[1].baz': 5,
            'prefix[2]': 'test'}

        flattener = Flattener('prefix')

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_dict_with_list(self):
        source = {'foo': 1, 'bar': [2,3,4], 'baz': [{'foo': 5, 'bar': 6}, {'foo': [7, 8], 'bar': 9}]}
        expected = {
            'foo': 1,
            'bar[0]': 2,
            'bar[1]': 3,
            'bar[2]': 4,
            'baz[0].foo': 5,
            'baz[0].bar': 6,
            'baz[1].foo[0]': 7,
            'baz[1].foo[1]': 8,
            'baz[1].bar': 9}

        flattener = Flattener()

        self.assertEqual(flattener.flatten(source), expected)

    def test_flattening_set(self):
        source = {1,2,3,4,5,6,7,8}
        flattener = Flattener('pr')

        result = flattener.flatten(source)
        expected_keys = {'pr[0]', 'pr[1]', 'pr[2]', 'pr[3]', 'pr[4]', 'pr[5]', 'pr[6]', 'pr[7]'}
        expected_values = {1,2,3,4,5,6,7,8}
        self.assertEqual(result.keys(), expected_keys)
        self.assertEqual(set(result.values()), expected_values)

if __name__ == '__main__':
    unittest.main()
