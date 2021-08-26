import unittest
from calc import Calc

class TestCalculationMethods(unittest.TestCase):

    def setUp(self):
        self.c = Calc()

    # addition
    def testAddNumbers(self):
        c = Calc()
        self.assertEqual(self.c.add(2,2), 4)
    
    def testMultiplication(self):
        c = Calc()
        self.assertEqual(self.c.mul(1,5), 5)

    def testNegativeNumbers(self):
        c = Calc()
        self.assertEqual(self.c.add(-4,-4), -8)

    
if __name__== '__main__':
    unittest.main()