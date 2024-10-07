from unittest import TestCase

from myPythonCode.classTask.get_single_string import single

class TestGetSingleString(TestCase):
    def test_get_single_string(self):
        self.assertEqual(single( 'abc','xyz'),'xycabz')
