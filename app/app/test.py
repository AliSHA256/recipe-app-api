from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding numbers together"""
        """
        self is used to access 
        methods and attributes of the
        SimpleTestCase class, which CalcTests inherits from.
        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(12, 15)
        self.assertEqual(res, -3)
