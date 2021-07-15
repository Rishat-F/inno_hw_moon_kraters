from typing import List


def calculate(moon_matrix: List[List]) -> int:
    """Count a quantity of kraters.

    Args:
        moon_matrix: Two-dimensional list of 0 and 1.
            Its a simplified representation of moon area snapshot.
            Where 1 matches valley, 0 matches flat area.

    Returns:
        The quantity of kraters.
    """
    krater_count = 0
    for i in range(len(moon_matrix)):
        for j in range(len(moon_matrix[i])):
            if i == 0:
                if j == 0:
                    if moon_matrix[i][j] == 1:
                        krater_count += 1
                elif moon_matrix[i][j - 1] == 0 and moon_matrix[i][j] == 1:
                    krater_count += 1
            elif j == 0:
                if moon_matrix[i - 1][j] == 0 and moon_matrix[i][j] == 1:
                    krater_count += 1
            else:
                if moon_matrix[i][j] == 1 and moon_matrix[i][j - 1] == 0 and moon_matrix[i - 1][j] == 0:
                    krater_count += 1
    return krater_count


if __name__ == '__main__':
    pass
