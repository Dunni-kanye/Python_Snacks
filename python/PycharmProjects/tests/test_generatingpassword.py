import string
from unittest import TestCase

from myPythonCode.classTask.generatingpassword import generate_password
class TestGeneratingPassword(TestCase):
    def test_password_length(self):
        password = generate_password(8)
        self.assertEqual(len(password), 8)


    def test_password_letters(self):
        password = generate_password(12)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_contains_special_characters(self):
        password = generate_password(12)
        self.assertTrue(any(c in string.puntuation for c in password))

