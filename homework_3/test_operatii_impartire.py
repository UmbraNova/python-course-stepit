import unittest
import operatii_impartire

class TestOperatiiImpartire(unittest.TestCase):
    def test_normala(self):
        self.assertEqual(operatii_impartire.impartire_normala(4, 2), 2)
    def test_intreaga(self):
        self.assertEqual(operatii_impartire.impartire_intreaga(5, 2), 2)
    def test_rest(self):
        self.assertEqual(operatii_impartire.impartire_rest(7, 3), 1)
