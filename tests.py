import unittest

from euler11 import (
    get_number_combinations, max_product_for_line,
    parse_columns, parse_line, parse_rows
)


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

    def test_max_product_of_single_line(self):
        self.assertEqual(max_product_for_line("1 2 3 4", 4), 24)
        self.assertEqual(max_product_for_line("1 2 3 4 5", 4), 120)

    def test_parse_rows_from_grid(self):
        grid = "1 2 3\n" + \
               "4 5 6\n" + \
               "7 8 9"
        self.assertEqual(parse_rows(grid), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_parse_columns_from_grid(self):
        grid = "1 2 3\n" + \
               "4 5 6\n" + \
               "7 8 9"
        self.assertEqual(
            parse_columns(grid),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        )


if __name__ == "__main__":
    unittest.main()
