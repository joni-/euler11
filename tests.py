import unittest

from euler11 import get_number_combinations, parse_line


class ParsingTests(unittest.TestCase):

    def test_parse_numbers_from_line(self):
        self.assertEqual(parse_line("1 2 3 4"), [1, 2, 3, 4])
        self.assertEqual(parse_line("00 01 02 03"), [0, 1, 2, 3])

    def test_list_of_numbers_from_line(self):
        self.assertEqual(get_number_combinations("1 2 3 4", 4), [[1, 2, 3, 4]])
        self.assertEqual(
            get_number_combinations("1 2 3 4 5", 4),
            [[1, 2, 3, 4], [2, 3, 4, 5]]
        )


if __name__ == "__main__":
    unittest.main()
