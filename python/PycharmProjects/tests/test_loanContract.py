import unittest
from datetime import datetime

from myPythonCode.loanContract import LoanContract
from datetime import datetime


class TestLoanContract(unittest.TestCase):

    def test_create_loan_contract(self):
        loan = LoanContract("Dunni Baby", 5.0,10000, 5)
        self.assertIsNotNone(loan)
        self.assertEqual(loan.borrower, "Dunni Baby")
        self.assertEqual(loan.interest_rate, 5.0)
        self.assertEqual(loan.loan_amount, 10000)
        self.assertEqual(loan.loan_period, 5)

    def test_get_borrower(self):
        name = "Dunni Baby"
        loan = LoanContract("Dunni Baby", 5.0,10000, 5)
        self.assertTrue(loan)
        self.assertEqual(loan.get_borrower(), "Dunni Baby")

    def test_set_borrower(self):
        loan = LoanContract("Dunni Baby", 5.0,10000, 5)
        self.assertTrue(loan)
        new_borrower = "Dunni Love"
        loan.set_borrower(new_borrower)
        self.assertEqual(loan.get_borrower(), "Dunni Love")


    def test_get_interest(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        loan.interest_rate = 5.5
        self.assertTrue(loan)

    def test_set_interest(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        loan.set_interest_rate(5.5)
        self.assertTrue(loan.get_interest_rate(), 5.5)

    def test_set_loan_period(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        loan.set_loan_period(5)
        self.assertEqual(loan.loan_period, 5)

    def test_get_loan_period(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        self.assertEqual(loan.get_loan_period(),5)

    def test_get_loan_amount(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        loan.loan_amount = 10000
        self.assertEqual(loan.loan_amount, 10000)

    def test_set_loan_amount(self):
        loan = LoanContract("Dunni Love", 5.0,10000, 5)
        loan.set_loan_amount(10000)
        self.assertEqual(loan.loan_amount, 10000)

    def test_compute_monthly_payment(self):
        loan = LoanContract("Dunni Love", 5.0, 10000, 5)
        loan_amount = 10000
        annual_interest_rate = 5.0
        loan_period_years = 5

        monthly_interest_rate = annual_interest_rate / 12 / 100
        total_number_of_payments = loan_period_years * 12

        expected_monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_number_of_payments)
        self.assertAlmostEqual(loan.compute_monthly_payment(), expected_monthly_payment, places=2)


