from unittest import TestCase
from myPythonCode.classTask.alphabetcheck import alphabet_dict
class TestAlphabet(TestCase):
    def test_alphabet(self):
        self.assertEsiqual(alphabet_dict("bimbola"), {'a': 1, 'b': 2, 'i': 1, 'm': 1, 'l': 1, 'o': 1})
        self.assertEqual(alphabet_dict("Bimbola"), {'a': 1, 'b': 2, 'i': 1, 'm': 1, 'l': 1, 'o': 1})