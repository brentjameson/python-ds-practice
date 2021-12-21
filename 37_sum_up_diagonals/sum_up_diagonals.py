def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    empty_list = []

    tl_br = 0
    tr_bl = -1

    for array in matrix:
        empty_list.append(array[tl_br])
        empty_list.append(array[tr_bl])
        tl_br = tl_br + 1
        tr_bl = tr_bl -1
    return sum(empty_list)

m1 = [
[1,   2],
[30, 40],
]

m2 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]