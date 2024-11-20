"""
Module de tests unitaires pour tester la fonction multiplication.
"""

import unittest
from app import multiplication

class TestMultiplication(unittest.TestCase):
    """
    Classe contenant des tests unitaires pour la fonction multiplication.
    """

    def test_multiplication_true(self):
        """
        Vérifie que la multiplication retourne le bon résultat.
        """
        self.assertEqual(multiplication(2, 5), 10)

    def test_multiplication_not_true(self):
        """
        Vérifie que la multiplication ne retourne pas un résultat incorrect.
        """
        self.assertNotEqual(multiplication(2, 5), 11)

if __name__ == '__main__':
    unittest.main()

