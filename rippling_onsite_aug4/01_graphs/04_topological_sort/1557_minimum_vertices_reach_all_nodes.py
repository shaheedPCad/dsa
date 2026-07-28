# LC 1557: Minimum Number of Vertices to Reach All Nodes
#
# You are given a directed acyclic graph with n vertices numbered 0 through
# n - 1. Each edge [from_node, to_node] is directed from from_node to to_node.
#
# Return the smallest set of vertices from which all nodes in the graph are
# reachable. The solution is guaranteed to be unique, and any order is valid.


# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
n_one = 6
edges_one = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
expected_one = [0, 3]

n_two = 5
edges_two = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
expected_two = [0, 2, 3]
