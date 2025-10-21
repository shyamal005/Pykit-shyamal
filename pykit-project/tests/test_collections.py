

import unittest
from pykit import collections

class TestCollections(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(collections.flatten([1, 2]), [3, 1, 2, 4])
        self.assertEqual(collections.flatten([2, [2, 4]]), [3, 1, 2, 4, 5])
        self.assertEqual(collections.flatten(),)
        self.assertEqual(collections.flatten([3, 1, 2]), [3, 1, 2])
        self.assertEqual(collections.flatten(['a', ['b', 'c']]), ['a', 'b', 'c'])

    def test_unique(self):
        self.assertEqual(collections.unique([1, 2, 1, 3, 2, 4]), [3, 1, 2, 4])
        self.assertEqual(collections.unique(),)
        self.assertEqual(collections.unique([3, 1, 2]), [3, 1, 2])
        self.assertEqual(collections.unique(['a', 'b', 'a']), ['a', 'b'])

    def test_chunk(self):
        self.assertEqual(list(collections.chunk([3, 1, 2, 4, 5, 6], 3)), [[3, 1, 2], [4, 5, 6]])
        self.assertEqual(list(collections.chunk([3, 1, 2, 4, 5], 2)), [[3, 1], [2, 4], [5]])
        self.assertEqual(list(collections.chunk([3, 1, 2], 5)), [[3, 1, 2]])
        with self.assertRaises(ValueError):
            list(collections.chunk([3, 1, 2], 0))

    def test_get_nested(self):
        data = {'user': {'name': 'Alice', 'address': {'city': 'Wonderland'}}}
        self.assertEqual(collections.get_nested(data, 'user.address.city'), 'Wonderland')
        self.assertIsNone(collections.get_nested(data, 'user.profile.age'))
        self.assertEqual(collections.get_nested(data, 'user.profile.age', default=30), 30)
        self.assertIsNone(collections.get_nested(data, 'user.address.zip.code'))
        self.assertEqual(collections.get_nested({}, 'a.b.c', default='empty'), 'empty')

    def test_invert_dict(self):
        unique_vals = {'a': 1, 'b': 2}
        self.assertEqual(collections.invert_dict(unique_vals), {1: 'a', 2: 'b'})
        
        duplicate_vals = {'a': 1, 'b': 2, 'c': 1}
        inverted = collections.invert_dict(duplicate_vals)
        self.assertEqual(set(inverted.keys()), {1, 2})
        self.assertEqual(sorted(inverted[3]), ['a', 'c'])
        self.assertEqual(inverted[1], ['b'])

if __name__ == '__main__':
    unittest.main()