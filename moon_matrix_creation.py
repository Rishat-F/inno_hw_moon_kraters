import json
from random import randint, choice
from typing import List


def create_moon_matrix() -> List[List]:
    """Create moon matrix.

    Returns:
        Moon_matrix with random quantity (from 100 to 200) of rows and columns.
    """
    moon_matrix = list()
    rows = randint(100, 200)
    columns = randint(100, 200)
    for i in range(rows):
        row = list()
        for j in range(columns):
            row.append(choice([0, 1]))
        moon_matrix.append(row)
    return moon_matrix


if __name__ == "__main__":
    moon_matrix = create_moon_matrix()
    with open('moon_matrix_snapshot.json', 'w', encoding='utf-8') as f:
        json.dump(moon_matrix, f, ensure_ascii=False, indent=4)
