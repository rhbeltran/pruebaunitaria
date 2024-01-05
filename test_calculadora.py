# test_calculadora.py
import unittest
import calculadora

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.suma(2, 3), 5)
        self.assertEqual(calculadora.suma(2, -3), -1)
        self.assertEqual(calculadora.suma(0, 0), 0)
    def test_resta(self):
        self.assertEqual(calculadora.resta(2, 3), -1)
        self.assertEqual(calculadora.resta(2, -3), 5)
        self.assertEqual(calculadora.resta(0, 0), 0)
    def test_multiplicacion(self):
        self.assertEqual(calculadora.multiplicacion(2, 3), 6)
        self.assertEqual(calculadora.multiplicacion(2, -3), -6)
        self.assertEqual(calculadora.multiplicacion(0, 0), 0)
    def test_division(self):
        self.assertEqual(calculadora.division(2, 3), 2/3)
        self.assertEqual(calculadora.division(2, -3), 2/-3)
       
        with self.assertRaises(ValueError):
            calculadora.division(2, 0)

if __name__ == '__main__':
    unittest.main()