import unittest
from kalk import tambah, kurang, kali, bagi


class TestKalk(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-1, 1), 0)

    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)
        self.assertEqual(kurang(0, 5), -5)

    def test_kali(self):
        self.assertEqual(kali(4, 3), 12)
        self.assertEqual(kali(-2, 3), -6)

    def test_bagi(self):
        self.assertEqual(bagi(8, 2), 4)
        self.assertEqual(bagi(10, 4), 2.5)

    def test_bagi_nol(self):
        with self.assertRaises(ValueError):
            bagi(1, 0)


if __name__ == "__main__":
    unittest.main()
