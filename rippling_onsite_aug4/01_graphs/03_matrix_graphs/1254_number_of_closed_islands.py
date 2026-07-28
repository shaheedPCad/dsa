# LC 1254: Number of Closed Islands
#
# You are given a 2D grid of 0s and 1s. A 0 represents land and a 1
# represents water.
#
# An island is a maximal 4-directionally connected group of 0s. A closed
# island is an island completely surrounded by 1s on all four sides.
#
# Return the number of closed islands.

from collections import deque

def closedIsland(grid):
  rows = len(grid)
  cols = len(grid[0])

  visited = set()
  queue = deque()

  next_pos_diff = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
  ]

  def bfs(row, col):

    is_closed = True

    visited.add((row, col))
    queue.append((row, col))


    while queue:
      row, col = queue.popleft()

      if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        is_closed = False

      for next_row_diff, next_col_diff in next_pos_diff:
        next_row = row + next_row_diff
        next_col = col + next_col_diff

        if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 and (next_row, next_col) not in visited:
          visited.add((next_row, next_col))
          queue.append((next_row, next_col))

    

    return is_closed



  closed_count = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 0 and (r, c) not in visited:
        if bfs(r, c) is True:
          closed_count += 1
      

  return closed_count




# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
grid_one = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
expected_one = 2

grid_two = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
]
expected_two = 1

grid_three = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
expected_three = 2
