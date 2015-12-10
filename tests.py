import unittest

from euler11 import (
    get_number_combinations, max_product_for_line,
    parse_columns, parse_diagonal_lines, parse_grid, parse_line, parse_rows
)


class ParsingTests(unittest.TestCase):

    def setUp(self):
        self.grid = "1 2 3\n" + \
                    "4 5 6\n" + \
                    "7 8 9"

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
        self.assertEqual(
            parse_rows(self.grid),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        )

    def test_parse_columns_from_grid(self):
        self.assertEqual(
            parse_columns(self.grid),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        )

    def test_parse_diagonal_lines_from_grid(self):
        self.assertEqual(
            parse_diagonal_lines(self.grid),
            [[1, 5, 9], [3, 5, 7]]
        )

    def test_parse_grid(self):
        self.assertEqual(
            parse_grid(self.grid),
            [
                [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
                [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
                [1, 5, 9], [3, 5, 7]  # diagonals
            ]
        )


if __name__ == "__main__":
    unittest.main()
