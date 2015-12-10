def parse_line(line):
    """ Parses given line into list of numbers.
    e.g. '1 2 3 4' => [1, 2, 3, 4] """
    return [int(num) for num in line.split()]


def get_number_combinations(line, n):
    """ Parses given line into lists of numbers of length n and returns them as
    a list.
    e.g. line: '1 2 3 4 5', n: 4 => [[1, 2, 3, 4], [2, 3, 4, 5]] """
    numbers = parse_line(line)
    result = []
    start = 0
    end = n
    while end <= len(numbers):
        result.append(numbers[start:end])
        start += 1
        end += 1
    return result


def max_product_for_line(line, n):
    """ Parses given line into lists of numbers of length n, multiplies the
    numbers in each list together and returns the maximum product. """
    products = []
    for numbers in get_number_combinations(line, n):
        result = 1
        for n in numbers:
            result *= n
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
