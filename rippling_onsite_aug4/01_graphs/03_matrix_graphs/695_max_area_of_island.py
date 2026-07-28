# LC 695: Max Area of Island
#
# You are given an m x n binary matrix grid. An island is a group of 1s
# connected 4-directionally (up, down, left, right). The area of an island is
# the number of cells containing 1 in that island.
#
# Return the maximum area of an island. If there is no island, return 0.

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_island_size = 0

    next_pos_diff = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    
    def dfs(row, col):

        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0

        grid[row][col] = 0
        area = 1

        for next_row_diff, next_col_diff, in next_pos_diff:
            next_row = row + next_row_diff
            next_col = col + next_col_diff


            area += dfs(next_row, next_col)


        return area


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                curr_area = dfs(r, c)

                max_island_size = max(curr_area, max_island_size)


    return max_island_size

  
  

# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
grid_one = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
expected_one = 6

print(maxAreaOfIsland(grid_one))

grid_two = [[0, 0, 0, 0, 0, 0, 0, 0]]
expected_two = 0
