# LC 1020: Number of Enclaves
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and
# 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent
# 4-directionally land cell or walking off the boundary of the grid.
#
# Return the number of land cells for which we cannot walk off the boundary of
# the grid in any number of moves.

from collections import deque

def numEnclaves(grid):
    rows = len(grid)
    cols = len(grid[0])


    queue = deque()

    # top row
    for c in range(cols):
        if grid[0][c] == 1:
            grid[0][c] = 0
            queue.append((0, c))

    # bottom row
    for c in range(cols):
        if grid[rows - 1][c]:
            grid[rows - 1][c] = 0
            queue.append((rows - 1, c))


    # left side
    for r in range(1, rows - 1):
        if grid[r][0] == 1:
            grid[r][0] = 0
            queue.append((r, 0))

    # right side
    for r in range(1, rows - 1):
        if grid[r][cols - 1] == 1:
            grid[r][cols - 1] = 0
            queue.append((r, cols - 1))


    next_pos_diff = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]


    while queue:
        row, col = queue.popleft()

        for next_row_diff, next_col_diff in next_pos_diff:
            next_row = row + next_row_diff
            next_col = col + next_col_diff

            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                grid[next_row][next_col] = 0
                queue.append((next_row, next_col))



    enclaves = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                enclaves += 1


    return enclaves


# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
grid_one = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]
expected_one = 3

grid_two = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
]
expected_two = 0

print(numEnclaves(grid_one))
