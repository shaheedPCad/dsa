"""Practice: 1306. Jump Game III

Do not look up the solution yet.

From index i, you may jump to i + arr[i] or i - arr[i]. Return True if an
index containing 0 can be reached without leaving the array.
"""

from collections import deque

def canReach(arr, start):

    n = len(arr)

    visited = set([start])

    queue = deque([start])


    while queue:
        node = queue.popleft()

        if arr[node] == 0:
            return True


        jump_val = arr[node]

        new_left = (node - jump_val) if (node - jump_val) >= 0 else None
        new_right = (node + jump_val) if (node + jump_val) <= (n - 1) else None

        if new_left is not None and new_left not in visited:
            visited.add(new_left)
            queue.append(new_left)

        if new_right is not None and new_right not in visited:
            visited.add(new_right)
            queue.append(new_right)



    return False





# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
arr_one = [4, 2, 3, 0, 3, 1, 2]
start_one = 5
expected_one = True

arr_two = [4, 2, 3, 0, 3, 1, 2]
start_two = 0
expected_two = True

arr_three = [3, 0, 2, 1, 2]
start_three = 2
expected_three = False


print(canReach(arr_one, start_one))


# -------------------------------------------------
# Before coding, explain the problem
# -------------------------------------------------
# 1. What represents a graph node?
# 2. What are the possible neighbors of index i?
# 3. How do you prevent a jump outside the array?
# 4. What condition means we have succeeded?
# 5. Why do we need a visited set?
# 6. Why is BFS or DFS appropriate?
# 7. What should one queue/stack item contain?
#
# After implementing your method, test it with:
# result_one = your_method_here(arr_one, start_one)
# result_two = your_method_here(arr_two, start_two)
# result_three = your_method_here(arr_three, start_three)
#
# assert result_one == expected_one
# assert result_two == expected_two
# assert result_three == expected_three
