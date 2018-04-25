neighbors = {"0": ["8"],
             "1": ["2", "4"],
             "2": ["1", "3", "5"],
             "3": ["2", "6"],
             "4": ["1", "5", "7"],
             "5": ["2", "4", "6", "8"],
             "6": ["3", "5", "9"],
             "7": ["4", "8"],
             "8": ["5", "7", "9", "0"],
             "9": ["6", "8"],
             }


def get_neighbors(n):
    result = neighbors[n][:]
    result.append(n)

    return result


def increment_indices(indices, possibilities):
    indices = indices[:]
    indices[-1] += 1

    for i in range(len(indices) - 1, -1, -1):
        overflow = len(possibilities[i]) == indices[i]

        if overflow and i == 0:
            return None

        if overflow:
            indices[i] = 0
            indices[i-1] += 1

    return indices


def get_pins(observed):
    possibilities = list(map(get_neighbors, observed))

    indices = [0] * len(possibilities)

    result = []

    while indices is not None:
        combo = ""
        for possible_digits, index in zip(possibilities, indices):
            combo += possible_digits[index]
        result.append(combo)
        indices = increment_indices(indices, possibilities)

    return result


print(get_pins("12"))