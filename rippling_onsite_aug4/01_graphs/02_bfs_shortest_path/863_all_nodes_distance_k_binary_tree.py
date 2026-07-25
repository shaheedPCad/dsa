"""Practice: 863. All Nodes Distance K in Binary Tree

Do not look up the solution yet.

Return the values of all nodes exactly k edges away from the target node.
The answer may be returned in any order.
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, target, k):

    # build parent dictionary
    parent = {}


    def dfs_tree(n):
        if n == None:
            return

        if n.val == target.val:
            return n

        if n.left:
            parent[n.left] = n
            tar = dfs_tree(n.left)
            if tar:
                return tar

        if n.right:
            parent[n.right] = n
            tar = dfs_tree(n.right)
            if tar:
                return tar


    target_node = dfs_tree(root)


    queue = deque([(target_node, 0)])

    visited = set([target_node])

    res = []


    while queue:
        node, distance = queue.popleft()

        if distance == k:
            res.append(node.val)
            continue

        # explore parent
        if parent.get(node) is not None and parent[node] not in visited:
            visited.add(parent[node])
            queue.append((parent[node], distance + 1))


        if node.left is not None and node.left not in visited:
            visited.add(node.left)
            queue.append((node.left, distance + 1))


        if node.right is not None and node.right not in visited:
            visited.add(node.right)
            queue.append((node.right, distance + 1))



    return res

# -------------------------------------------------
# Practice examples
# -------------------------------------------------
# Tree represented in level-order form:
# root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# target value = 5
# k = 2
# expected values = [7, 4, 1]

# Second example:
# root = [1]
# target value = 1
# k = 3
# expected values = []


# -------------------------------------------------
# Before coding, explain the problem
# -------------------------------------------------
# 1. What represents a node in this graph?
# 2. What are the possible neighbors of a tree node?
# 3. Why are child pointers alone insufficient for this problem?
# 4. How could you move from a node to its parent?
# 5. What should the BFS queue store?
# 6. What does the distance k represent: nodes or edges?
# 7. When should a node be added to the answer?
# 8. How will you prevent revisiting nodes?
#
# After implementing your method, test it against the examples above.
