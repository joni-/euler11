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
