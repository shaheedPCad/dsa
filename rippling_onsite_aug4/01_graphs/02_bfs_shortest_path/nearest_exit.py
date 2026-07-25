"""Practice: Nearest Exit from Entrance in Maze

Do not look up the solution yet.

Your task:
    Return the number of steps from the entrance to the nearest reachable
    border cell that contains '.'. The entrance itself does not count.
"""

from collections import deque

def nearestExit(maze, entrance):
    rows = len(maze)
    cols = len(maze[0])

    visited = set([(entrance[0], entrance[1])])
    queue = deque([(entrance[0], entrance[1], 0)])

    while queue:
        row, col, steps_from_entrance = queue.popleft()

        if ((row == 0) or (row == rows - 1) or (col == 0) or (col == cols - 1)) and maze[row][col]  == "." and [row, col] != entrance:
            return steps_from_entrance


        up = row - 1 if row > 0 else None
        down = row + 1 if row < rows - 1 else None
        left = col - 1 if col > 0 else None
        right = col + 1 if col < cols - 1 else None

        if up != None and (up, col) not in visited and maze[up][col] != "+":
            visited.add((up, col))
            queue.append((up, col, steps_from_entrance + 1))

        if down != None and (down, col) not in visited and maze[down][col] != "+":
            visited.add((down, col))
            queue.append((down, col, steps_from_entrance + 1))

        if left != None and (row, left) not in visited and maze[row][left] != "+":
            visited.add((row, left))
            queue.append((row, left, steps_from_entrance + 1))

        if right != None and (row, right) not in visited and maze[row][right] != "+":
            visited.add((row, right))
            queue.append((row, right, steps_from_entrance + 1))




    return -1










# -------------------------------------------------
# Practice test casec
# -------------------------------------------------
maze = [
    ["+", "+", ".", "+"],
    [".", ".", ".", "+"],
    ["+", "+", "+", "."],
]

entrance = [1, 2]
expected_output = 1

print(nearestExit(maze, entrance))


# Before coding, answer these questions:
# 1. Why is BFS appropriate here?
# 2. What should one queue item contain?
# 3. When should a cell be marked visited?
# 4. What makes a cell an exit?
# 5. How do you make sure the entrance does not count?


# After implementing your method, test it using:
# result = your_solution_here(maze, entrance)
# assert result == expected_output
