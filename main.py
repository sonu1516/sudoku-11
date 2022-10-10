board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# We shorten the board name to bo for easy usage
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        # This prints a horizontal line between the bigger boxes
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


# This prints a vertical line between the bigger boxes
print_board(board)


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                # print("(", i, j, ")")
                return (i, j)
    return None


def valid(bo, num, pos):
    # We first check if the number has occurred within the row
    for i in range(len(bo[0])):
        # print(pos[0], [i], '----', (pos[1] != i))
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # We then check if the number has occurred within the column
    for i in range(len(bo)):  # checking column
        # print(bo[i][pos[1]], '----', (pos[0] != i))
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # We finally check if the number has occurred within the bigger box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # print("box_x = ", box_x)
    # print("box_y = ", box_y)
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        # This means that the find function came back null.
        # This implies that the sudoku has been solved.
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            # If the number can be plugged in at the empty slot, we insert it.
            bo[row][col] = i
            # We then recall the function to solve the next empty slot.
            if solve(bo):
                return True
            # When we run into an error, we backtrack.
            # We do this by placing a zero to the previously solved slot.
            bo[row][col] = 0
    return False


print_board(board)
solve(board)
print("Solving")
print_board(board)
