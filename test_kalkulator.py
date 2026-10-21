import unittest
from kalkulator import tambah, kurang

class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-1, 1), 0)

    def test_kurang(self):
        self.assertEqual(kurang(5, 2), 3)
        self.assertEqual(kurang(0, 4), -4)

if __name__ == '__main__':
    unittest.main()
