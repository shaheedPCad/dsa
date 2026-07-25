"""Practice: 542. 01 Matrix

Do not look up the solution yet.

For every cell, return its Manhattan distance to the nearest cell containing
0. Moving up, down, left, or right costs one step.
"""

from collections import deque

def updateMatrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    queue = deque()

    distance_mat = [[-1 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 1:
                distance_mat[row][col] = -1
            elif mat[row][col] == 0:
                distance_mat[row][col] = 0
                queue.append((row, col, 0))



    while queue:
        row, col, steps = queue.popleft()

        next_positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for next_pos in next_positions:
            row_change, col_change = next_pos
            next_row = row + row_change
            next_col = col + col_change

            if (0 <= next_row < rows) and (0 <= next_col < cols) and distance_mat[next_row][next_col] == -1:
                distance_mat[next_row][next_col] = steps + 1
                queue.append((next_row, next_col, steps + 1))





    return distance_mat



# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
matrix_one = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
expected_one = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

matrix_two = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]
expected_two = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 2, 1],
]


# -------------------------------------------------
# Before coding, explain the strategy
# -------------------------------------------------
# 1. Why is this a multi-source BFS problem?
# 2. Which cells should be placed in the queue initially?
# 3. What distance should each initial cell have?
# 4. What should the distance of a neighboring cell be?
# 5. When should a cell be marked visited?
# 6. Why is starting BFS from every zero better than starting from each one?
# 7. What should happen when the input matrix contains only one value type?
#
# After implementing your method, test it with:
# result_one = your_method_here(matrix_one)
# result_two = your_method_here(matrix_two)
#
# assert result_one == expected_one
# assert result_two == expected_two
