import unittest
from to_flat_array2_7 import to_flat, print_flat

##
# Test unpacking nested array into flat array
##
class ToFlatTestCase(unittest.TestCase):
    ca = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    na = [0,[1,2,3],[[[4],[5]],[6]],[7,8],9]

    """Tests for `to_flat_array2_7.py`."""

    def test_to_flat(self):
        """Is result a flat array?"""
        self.assertEqual(to_flat(ToFlatTestCase.na),ToFlatTestCase.ca)

if __name__ == '__main__':
    unittest.main()
