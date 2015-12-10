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


def parse_diagonal_lines(grid):
    """ Parses the grid and returns diagonal lines as a list of lists of ints.
    """
    rows = parse_rows(grid)

    # top left to bottom right
    from_topleft = []
    column = 0
    for row in rows:
        from_topleft.append(row[column])
        column += 1

    # top right to bottom left
    from_topright = []
    column = len(rows) - 1
    for row in rows:
        from_topright.append(row[column])
        column -= 1

    return [from_topleft, from_topright]


def parse_grid(grid):
    return parse_rows(grid) + parse_columns(grid) + parse_diagonal_lines(grid)
