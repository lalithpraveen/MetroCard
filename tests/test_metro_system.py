import unittest
from unittest.mock import patch, Mock
from card import Card
from file_reader import File_reader
from controller import Controller
from prices import Prices


class TestCard(unittest.TestCase):
    def test_deduct_cost_with_positive_balance(self):
        card = Card("MC1", 100)
        recharge_cost = card.deduct_cost(50)
        self.assertEqual(recharge_cost, 0)
        self.assertEqual(card.get_amount(), 50)

    def test_deduct_cost_with_insufficient_balance(self):
        card = Card("MC2", 30)
        recharge_cost = card.deduct_cost(50)
        self.assertEqual(recharge_cost, 21.0)  # Recharge cost + service fee
        self.assertEqual(card.get_amount(), 0)


class TestFileReader(unittest.TestCase):
    @patch('builtins.open')
    def test_readfile(self, mock_open):
        mock_file = Mock()
        mock_file.readlines.return_value = [
            "BALANCE MC1 100",
            "CHECK_IN MC1 ADULT CENTRAL",
            "PRINT_SUMMARY"
        ]
        mock_open.return_value = mock_file

        summary = {}  # Provide a mock summary here
        possible_return_trip = {}  # Provide a mock possible_return_trip here

        file_reader = File_reader(mock_file, summary, possible_return_trip)
        file_reader.readfile()


class TestPrices(unittest.TestCase):
    def test_get_price(self):
        prices = Prices()
        adult_price = prices.get_price("ADULT")
        self.assertEqual(adult_price, 200)

        kid_price = prices.get_price("KID")
        self.assertEqual(kid_price, 50)

        senior_price = prices.get_price("SENIOR_CITIZEN")
        self.assertEqual(senior_price, 100)

    def test_get_discount(self):
        prices = Prices()
        adult_discount = prices.get_discount("ADULT", return_trip=True)
        self.assertEqual(adult_discount, 100)

        kid_discount = prices.get_discount("KID", return_trip=False)
        self.assertEqual(kid_discount, 0)

        senior_discount = prices.get_discount("SENIOR_CITIZEN", return_trip=True)
        self.assertEqual(senior_discount, 50)


if __name__ == '__main__':
    unittest.main()
