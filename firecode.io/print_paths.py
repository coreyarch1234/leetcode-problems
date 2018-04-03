
total_path = []
def print_paths(board, path = [], pos = [0, 0]):
    if len(path) == 0:
        current = board[0][0]
        path.append(current)
    row_len = len(board[0])
    col_len = len(board)
    start = board[0][0]
    end = board[col_len - 1][row_len - 1]

    next_right = pos[1] + 1
    next_down = pos[0] + 1
    print 'pos',pos
    # next right
    if next_right < row_len and next_down < col_len:
        print 'board',board
        path.append(board[pos[0]][next_right])
        return print_paths(board, path, [pos[0], next_right])
    # next_down
    if next_down < col_len and next_right < row_len:
        path.append(board[next_down][pos[0]])
        return print_paths(board, path, [next_down, pos[0]])
    if board[pos[0]][pos[1]] == end:
        print 'they are equal'
    print 'next_down, next_right',[next_down, next_right]
    # path.append(board[next_down][next_right])
    # total_path + = path
    # return total_path

print print_paths([['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']])
