import unittest

import roman_numerals

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class RomanNumeralsTest(unittest.TestCase):
    numerals = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        9: 'IX',
        27: 'XXVII',
        48: 'XLVIII',
        49: 'XLIX',
        59: 'LIX',
        93: 'XCIII',
        141: 'CXLI',
        163: 'CLXIII',
        402: 'CDII',
        575: 'DLXXV',
        911: 'CMXI',
        1024: 'MXXIV',
        3000: 'MMM',
    }

    def test_numerals(self):
        for arabic, numeral in self.numerals.items():
            self.assertEqual(roman_numerals.roman(arabic), numeral)


if __name__ == '__main__':
    unittest.main()
