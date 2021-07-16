from pprint import pprint
from random import randint, choice
from typing import Generator


def generator(n: int) -> Generator:
    """Moon matrix generator function.

    Generate dicts including moon_matrix in key 'test_input'.

    Args:
        n: A quantity of dicts that should be generated.

    Returns:
        Generator-object.
    """
    for i in range(n):
        moon_matrix = list()
        rows = randint(5, 20)
        columns = randint(5, 20)
        for i in range(rows):
            row = list()
            for j in range(columns):
                row.append(choice([0, 1]))
            moon_matrix.append(row)
        yield {"test_input": moon_matrix, "expected": None}


if __name__ == "__main__":
    gen = generator(10)
    moon_snapshots = list()
    for elem in gen:
        moon_snapshots.append(elem)
    pprint(moon_snapshots)
