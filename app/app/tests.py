#Sample tests

from django.test import SimpleTestCase

from app import calc
#I have already tried:
# from app.app import calc or
#import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 12)
