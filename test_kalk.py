import unittest

from kalk import bagi, kali, kurang, tambah


class TestKalk(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)

    def test_kali(self):
        self.assertEqual(kali(4, 3), 12)

    def test_bagi(self):
        self.assertEqual(bagi(8, 2), 4)

    def test_bagi_nol_raises_valueerror(self):
        with self.assertRaises(ValueError):
            bagi(1, 0)


if __name__ == "__main__":
    unittest.main()
