# LC 417: Pacific Atlantic Water Flow
#
# You are given an m x n matrix heights. The Pacific Ocean touches the top and
# left edges. The Atlantic Ocean touches the bottom and right edges.
#
# Water can flow from a cell to a directly adjacent cell whose height is less
# than or equal to the current cell's height. Return all coordinates from which
# water can flow to both oceans.
from collections import deque

def pacificAtlantic(heights):
  rows = len(heights)
  cols = len(heights[0])

  pacific_queue = deque()
  pacific_visited = set()

  # add top row cells to pacific traversal queue
  for c in range(cols):
    pacific_visited.add((0, c))
    pacific_queue.append((0, c))


  # add left row cells to pacific traversal queue
  for r in range(1, rows):
    pacific_visited.add((r, 0))
    pacific_queue.append((r, 0))


  next_pos_diff = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
  ]

  # process pacific queue
  while pacific_queue:
    row, col = pacific_queue.popleft()

    for next_row_diff, next_col_diff in next_pos_diff:
      next_row = next_row_diff + row
      next_col = next_col_diff + col

      if 0 <= next_row < rows and 0 <= next_col < cols and heights[row][col] <= heights[next_row][next_col] and (next_row, next_col) not in pacific_visited:
        pacific_visited.add((next_row, next_col))
        pacific_queue.append((next_row, next_col))


  atlantic_queue = deque()
  atlantic_set = set()

  # add bottom row cells to atlantic traversal queue
  for c in range(cols):
    atlantic_set.add((rows - 1, c))
    atlantic_queue.append((rows - 1, c))


  # add right row cells to atlantic traversal queue
  for r in range(rows - 1):
    atlantic_set.add((r, cols - 1))
    atlantic_queue.append((r, cols - 1))

  # process pacific queue
  while atlantic_queue:
    row, col = atlantic_queue.popleft()

    for next_row_diff, next_col_diff in next_pos_diff:
      next_row = next_row_diff + row
      next_col = next_col_diff + col

      if 0 <= next_row < rows and 0 <= next_col < cols and heights[row][col] <= heights[next_row][next_col] and (next_row, next_col) not in atlantic_set:
        atlantic_set.add((next_row, next_col))
        atlantic_queue.append((next_row, next_col))


  result = []

  for row, col in pacific_visited & atlantic_set:
    result.append([row, col])


  return result





# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
heights_one = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]


expected_one = [
    [0, 4],
    [1, 3],
    [1, 4],
    [2, 2],
    [3, 0],
    [3, 1],
    [4, 0],
]

heights_two = [[1]]
expected_two = [[0, 0]]


