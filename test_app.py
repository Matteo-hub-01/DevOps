import unittest

from app import multiplication

class TestStringMethods(unittest.TestCase):

    def test_multiplicationTrue(self):
        self.assertEqual(multiplication(2,5),10)

    def test_multiplicatioNotTrue(self):
        self.assertNotEqual(multiplication(2,5),11)

if __name__ == '__main__':
    unittest.main() 
