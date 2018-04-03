# # Get all diagonals of matrix
# matrix = [[-2,  5,  3,  2],
#           [ 9, -6,  5,  1],
#           [ 3,  2,  7,  3],
#           [-1,  8, -4,  8]]
# should produce :
#
# [[-2], [9, 5], [3,-6, 3], [-1, 2, 5, 2], [8, 7, 1], [-4, 3], [8],
#  [2], [3,1], [5, 5, 3], [-2, -6, 7, 8], [9, 2, -4], [3, 8], [-1]]
#


def all_diagonals(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    t_l_diagonals_dict = {}
    b_l_diagonals_dict = {}
    for i in range(row_len):
        for j in range(col_len):
            if i + j not in b_l_diagonals_dict:
                b_l_diagonals_dict[i + j] = [matrix[i][j]]
            else:
                b_l_diagonals_dict[i + j].append(matrix[i][j])

            if j - i not in t_l_diagonals_dict:
                t_l_diagonals_dict[j - i] = [matrix[i][j]]
            else:
                t_l_diagonals_dict[j - i].append(matrix[i][j])
    return t_l_diagonals_dict.values() + b_l_diagonals_dict.values()

# matrix = [[-2,  5,  3,  2],
#           [ 9, -6,  5,  1],
#           [ 3,  2,  7,  3],
#           [-1,  8, -4,  8]]
matrix = [[-2,  5,  3,  2],
        [ 9, -6,  5,  1]]

print all_diagonals(matrix)
