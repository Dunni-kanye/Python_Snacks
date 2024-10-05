from unittest import TestCase
class TestGetSingleString(TestCase):
    def test_get_single_string(self):
        result = get_single_string.single('abc','xyz')
        self.assertEqual('xycabz', result)
