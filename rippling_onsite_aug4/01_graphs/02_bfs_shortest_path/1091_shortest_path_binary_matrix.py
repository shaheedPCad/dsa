"""Practice: 1091. Shortest Path in Binary Matrix

Do not look up the solution yet.

Find the shortest 8-directional path of zero cells from the top-left corner
to the bottom-right corner. Return the number of visited cells, or -1.
"""

from collections import deque

def shortestPathBinaryMatrix(grid):

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1


    visited = set([(0, 0)])
    queue = deque([(0, 0, 1)])

    while queue:
        row, col, distance = queue.popleft()

        if row == rows - 1 and col == cols - 1:
            return distance


        next_cell_arr = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]


        for next_row_diff, next_col_diff in next_cell_arr:
            next_row = row + next_row_diff
            next_col = col + next_col_diff

            if (0 <= next_row < rows and 0 <= next_col < cols) and (next_row, next_col) not in visited and grid[next_row][next_col] == 0:
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, distance + 1))


    return -1




# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
grid_one = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]
expected_one = 4

grid_two = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]
expected_two = -1


# -------------------------------------------------
# Before coding, explain the problem
# -------------------------------------------------
# 1. What are the start and target coordinates?
# 2. What does a clear cell represent?
# 3. How many directions can we move in?
# 4. What should one queue item store?
# 5. Why is BFS appropriate?
# 6. What should happen if the start or target is blocked?
# 7. Does the answer count edges or visited cells?
# 8. How will you prevent revisiting cells?
#
# After implementing your method, test it with:
# result_one = your_method_here(grid_one)
# result_two = your_method_here(grid_two)
#
# assert result_one == expected_one
# assert result_two == expected_two
