import sys


def parse_line(line):
    """ Parses given line into list of numbers.
    e.g. '1 2 3 4' => [1, 2, 3, 4] """
    return [int(num) for num in line.split()]


def get_number_combinations(numbers, n):
    """ Returns a list of lists of ints of length n from the given list of
    ints such that each n length list contains adjacent numbers.
    e.g. numbers: [1, 2, 3, 4, 5], n: 4 => [[1, 2, 3, 4], [2, 3, 4, 5]] """
    result = []
    start = 0
    end = n
    while end <= len(numbers):
        result.append(numbers[start:end])
        start += 1
        end += 1
    return result


def max_product_for_numbers(numbers, n):
    """ Returns max product for n adjacent numbers in the given list of numbers.
    """
    products = []
    for numbers in get_number_combinations(numbers, n):
        result = 1
        for num in numbers:
            result *= num
        products.append(result)
    return max(products)


def parse_rows(grid):
    """ Parses the grid and returns rows as a list of lists of ints. """
    return [parse_line(line) for line in grid.splitlines()]


def parse_columns(grid):
    """ Parses the grid and returns columns as a list of lists of ints. """
    columns = []
    rows = parse_rows(grid)
    for column in range(len(rows)):
        col_numbers = []
        for row in range(len(rows)):
            col_numbers.append(rows[row][column])
        columns.append(col_numbers)
    return columns


def parse_diagonal_lines(grid, n):
    """ Parses the grid and returns diagonal lines as a list of lists of ints.
        Returns only lists that contains atleast n items. """

    # Implementation taken from
    # http://analgorithmaday.blogspot.fi/2011/04/traverse-array-diagonally.html
    rows = parse_rows(grid)

    # Top right to bottom left
    right_to_left = []
    for slice_ in range(len(rows)*2-1):
        z = 0 if slice_ < len(rows) else slice_ - len(rows) + 1
        result = []
        for j in range(z, slice_-z+1):
            row = j
            column = (len(rows) - 1) - (slice_ - j)
            result.append(rows[row][column])
        if len(result) >= n:
            right_to_left.append(result)

    # Top left to bottom right
    left_to_right = []
    for slice_ in range(len(rows)*2-1):
        z = 0 if slice_ < len(rows) else slice_ - len(rows) + 1
        result = []
        for j in range(z, slice_-z+1):
            row = j
            column = slice_ - j
            result.append(rows[row][column])
        if len(result) >= n:
            left_to_right.append(result)

    return right_to_left + left_to_right


def parse_grid(grid, n):
    return parse_rows(grid) + parse_columns(grid) + \
           parse_diagonal_lines(grid, n)


def max_product(grid, n):
    """ Returns max product of n adjacent numbers from the grid. """
    lines = parse_grid(grid, n)
    products = []
    for line in lines:
        products.append(max_product_for_numbers(line, n))
    return max(products)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} filename [n]".format(sys.argv[0]))
        sys.exit()

    filename = sys.argv[1]
    n = 4
    if len(sys.argv) > 2:
        try:
            n = int(sys.argv[2])
        except ValueError:
            n = 4

    with open(filename) as f:
        grid = f.read()
    print(max_product(grid, n))
