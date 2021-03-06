import unittest

from euler11 import (
    get_number_combinations, max_product, max_product_for_numbers,
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

    def test_combinations_of_numbers(self):
        self.assertEqual(
            get_number_combinations([1, 2, 3, 4], 4),
            [[1, 2, 3, 4]]
        )
        self.assertEqual(
            get_number_combinations([1, 2, 3, 4, 5], 4),
            [[1, 2, 3, 4], [2, 3, 4, 5]]
        )

    def test_max_product_of_single_line(self):
        self.assertEqual(max_product_for_numbers([1, 2, 3, 4], 4), 24)
        self.assertEqual(max_product_for_numbers([1, 2, 3, 4, 5], 4), 120)

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
            parse_diagonal_lines(self.grid, 2),
            [[2, 6], [1, 5, 9], [4, 8], [2, 4], [3, 5, 7], [6, 8]]
        )
        self.assertEqual(
            parse_diagonal_lines(self.grid, 3),
            [[1, 5, 9], [3, 5, 7]]
        )

    def test_parse_grid(self):
        self.assertEqual(
            parse_grid(self.grid, 3),
            [
                [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
                [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
                [1, 5, 9], [3, 5, 7]  # diagonals
            ]
        )

    def test_grid_max_product(self):
        grid1 = "9 1 1 1 1\n" + \
                "1 9 1 1 1\n" + \
                "1 1 9 1 1\n" + \
                "1 1 1 9 1\n" + \
                "1 1 1 9 9"

        grid2 = "0 0\n" + \
                "0 0"

        self.assertEqual(max_product(self.grid, 1), 9)
        self.assertEqual(max_product(self.grid, 2), 72)
        self.assertEqual(max_product(self.grid, 3), 504)
        self.assertEqual(max_product(grid1, 1), 9)
        self.assertEqual(max_product(grid1, 2), 81)
        self.assertEqual(max_product(grid1, 3), 729)
        self.assertEqual(max_product(grid1, 4), 6561)
        self.assertEqual(max_product(grid1, 5), 59049)
        self.assertEqual(max_product(grid2, 1), 0)
        self.assertEqual(max_product(grid2, 2), 0)

if __name__ == "__main__":
    unittest.main()
