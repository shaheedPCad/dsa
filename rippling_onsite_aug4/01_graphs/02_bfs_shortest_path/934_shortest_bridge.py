"""Practice: 934. Shortest Bridge

Do not look up the solution yet.

There are exactly two islands in the binary grid. Return the smallest number
of water cells that must be flipped to connect them.
"""

from collections import deque

def shortestBridge(grid):
    rows = len(grid)
    cols = len(grid[0])

    first_island_coords = set()

    def dfs_first_island(row, col):

        first_island_coords.add((row, col))

        up = row - 1 if row > 0 else None
        down = row + 1 if row < rows - 1 else None
        left = col - 1 if col > 0 else None
        right = col + 1 if col < cols - 1 else None

        if up is not None and (up, col) not in first_island_coords and grid[up][col] == 1:
            dfs_first_island(up, col)

        if down is not None and (down, col) not in first_island_coords and grid[down][col] == 1:
            dfs_first_island(down, col)

        if left is not None and (row, left) not in first_island_coords and grid[row][left] == 1:
            dfs_first_island(row, left)

        if right is not None and (row, right) not in first_island_coords and grid[row][right] == 1:
            dfs_first_island(row, right)

        return




    # find the first land cell
    found_first_island = False
    for row in range(rows):
        if found_first_island:
            break
        for col in range(cols):
            if grid[row][col] == 1:
                found_first_island = True
                dfs_first_island(row, col)
                break



    queue = deque()
    visited = set()
    
    for row, col in first_island_coords:
        queue.append((row, col, 0))


    visited.update(first_island_coords)



    while queue:
        row, col, distance = queue.popleft()

        up = row - 1 if row > 0 else None
        down = row + 1 if row < rows - 1 else None
        left = col - 1 if col > 0 else None
        right = col + 1 if col < cols - 1 else None


        if up is not None and grid[up][col] == 1 and (up, col) not in visited:
            return distance

        if down is not None and grid[down][col] == 1 and (down, col) not in visited:
            return distance

        if left is not None and grid[row][left] == 1 and (row, left) not in visited:
            return distance

        if right is not None and grid[row][right] == 1 and (row, right) not in visited:
            return distance

        if up is not None and (up, col) not in visited:
            visited.add((up, col))
            queue.append((up, col, distance + 1))

        if down is not None and (down, col) not in visited:
            visited.add((down, col))
            queue.append((down, col, distance + 1))


        if left is not None and (row, left) not in visited:
            visited.add((row, left))
            queue.append((row, left, distance + 1))

        if right is not None and (row, right) not in visited:
            visited.add((row, right))
            queue.append((row, right, distance + 1))



    return -1






# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
grid_one = [
    [0, 1],
    [1, 0],
]
expected_one = 1

grid_two = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1],
]
expected_two = 2

grid_three = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
expected_three = 1

print(shortestBridge(grid_three))


# -------------------------------------------------
# Before coding, explain the strategy
# -------------------------------------------------
# 1. Why might one DFS/BFS be needed before another BFS?
# 2. What should the first traversal identify?
# 3. What should the second traversal expand through?
# 4. When should a water cell's distance increase?
# 5. Why does BFS guarantee the smallest number of flips?
# 6. What should be stored in visited?
#
# Write your method and then test it with:
# result_one = your_method_here(grid_one)
# result_two = your_method_here(grid_two)
# result_three = your_method_here(grid_three)
#
# assert result_one == expected_one
# assert result_two == expected_two
# assert result_three == expected_three
