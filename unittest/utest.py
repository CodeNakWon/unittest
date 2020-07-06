#utest.py
import unittest
from portfolio import Portfolio

class PortfolioTest(unittest.TestCase):

    def test_empty(self):
        p = Portfolio()
        self.assertEqual(0.0, p.cost())#Success

    def test_google(self):
        p = Portfolio()
        p.buy('Google', 100, 176.48)
        #self.assertEqual(17648.0, p.cost())#Success
        self.assertEqual(0.0, p.cost())#Fail

    def test_yahoo(self):
        p = Portfolio()
        p.buy('Yahoo', 100, 36.15)
        self.assertEqual(3615.0, p.cost())#Success

if __name__ == '__main__':
    unittest.main()