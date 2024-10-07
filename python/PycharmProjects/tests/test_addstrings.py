   from unittest import TestCase

from myPythonCode.classTask.addstrings import combine_words
class TestAddToStrings(TestCase):
    def test_addstrings(self):
        self.assertEquals(combine_words("Hello", "Ce"),"Helcelo")


