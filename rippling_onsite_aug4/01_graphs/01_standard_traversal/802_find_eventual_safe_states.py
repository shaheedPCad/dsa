# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
# is an integer array of nodes adjacent to node i, meaning there is an edge from
# node i to each node in graph[i].
#
# A node is a terminal node if there are no outgoing edges. A node is a safe node
# if every possible path starting from that node leads to a terminal node (or
# another safe node).
#
# Return an array containing all the safe nodes of the graph. The answer should
# be sorted in ascending order.

from collections import deque

def eventualSafeNodes(graph):
    n = len(graph)

    adj_list = {i: [] for i in range(n)}
    outdegree = [0] * n

    for node in range(n):
        for nei in graph[node]:
            adj_list[nei].append(node)
            outdegree[node] += 1


    queue = deque()

    for i in range(n):
        if outdegree[i] == 0:
            queue.append(i)


    res = []

    while queue:
        node = queue.popleft()
        res.append(node)


        for nei in adj_list[node]:
            outdegree[nei] -= 1
            if outdegree[nei] == 0:
                queue.append(nei)



    return sorted(res)



# Example 1:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: Nodes 5 and 6 are terminal nodes. Every path starting at nodes
# 2, 4, 5, and 6 leads to either node 5 or 6.
#
# Example 2:
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation: Only node 4 is a terminal node, and every path starting from
# node 4 leads to node 4.
#
# Constraints:
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in strictly increasing order.
# The graph may contain self-loops.
# The number of edges is in the range [1, 4 * 10^4].


# Test case 1
test1 = [
    [1, 2],
    [2, 3],
    [5],
    [0],
    [5],
    [],
    [],
]
# Expected output: [2, 4, 5, 6]


# Test case 2
test2 = [
    [1, 2, 3, 4],
    [1, 2],
    [3, 4],
    [0, 4],
    [],
]
# Expected output: [4]

print(eventualSafeNodes(test2))
