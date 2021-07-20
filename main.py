import json
from typing import List

from scipy.ndimage.measurements import label


def calculate(moon_matrix: List[List]) -> int:
    """Count a quantity of kraters.

    Args:
        moon_matrix: Two-dimensional list of 0 and 1.
            Its a simplified representation of moon area snapshot.
            Where 1 matches valley, 0 matches flat area.

    Returns:
        The quantity of kraters.
    """
    return label(moon_matrix)[1]


if __name__ == "__main__":
    with open("moon_matrix_snapshot.json", "r", encoding="utf-8") as f:
        moon_matrix = json.load(f)
    print(calculate(moon_matrix))
