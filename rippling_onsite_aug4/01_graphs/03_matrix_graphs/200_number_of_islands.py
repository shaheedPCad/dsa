# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are
# surrounded by water.
#
# Example 1:
# Input: grid = [
#   ["1", "1", "1", "1", "0"],
#   ["1", "1", "0", "1", "0"],
#   ["1", "1", "0", "0", "0"],
#   ["0", "0", "0", "0", "0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1", "1", "0", "0", "0"],
#   ["1", "1", "0", "0", "0"],
#   ["0", "0", "1", "0", "0"],
#   ["0", "0", "0", "1", "1"]
# ]
# Output: 3
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


# Test case 1
test1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
# Expected output: 1


# Test case 2
test2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
# Expected output: 3
