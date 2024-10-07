from unittest import TestCase
from myPythonCode.classTask.validemail import validate_email

class TestValidemail(TestCase):
    def test_valid_email_is_true(self):
        self.assertEqual(validate_email("dunni18@gmail.com"), True)



