# You are given an integer n, the number of nodes in a directed graph where the
# nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and
# there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node
# ai to node bi in the graph, and
#
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node
# uj to node vj in the graph.
#
# Return an array answer of length n, where each answer[x] is the length of the
# shortest path from node 0 to node x such that the edge colors alternate along
# the path, or -1 if such a path does not exist.
#
# Example 1:
# Input: n = 3, redEdges = [[0, 1], [1, 2]], blueEdges = []
# Output: [0, 1, -1]
#
# Example 2:
# Input: n = 3, redEdges = [[0, 1]], blueEdges = [[2, 1]]
# Output: [0, 1, -1]
#
# Constraints:
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n

from collections import deque

def shortestAlternatingPaths(n, redEdges, blueEdges):

    adj_list = {i: [] for i in range(n)}

    for src, dest in redEdges:
        adj_list[src].append((dest, 'r'))

    for src, dest in blueEdges:
        adj_list[src].append((dest, 'b'))



    def bfs(end):

        visited = set([(0, '')])
        queue = deque([(0, '', 0)])

        while queue:
            node, prev_color, distance = queue.popleft()

            if node == end:
                return distance


            for nei, next_color in adj_list[node]:
                if (nei, next_color) not in visited and next_color != prev_color:
                    visited.add((nei, next_color))
                    queue.append((nei, next_color, distance + 1))




        return -1


    res = []
    for i in range(n):
        res.append(bfs(i))


    return res



    


# Test case 1
test1 = {
    "n": 3,
    "redEdges": [[0, 1], [1, 2]],
    "blueEdges": [],
}
# Expected output: [0, 1, -1]


# Test case 2
test2 = {
    "n": 3,
    "redEdges": [[0, 1]],
    "blueEdges": [[2, 1]],
}
# Expected output: [0, 1, -1]


print(shortestAlternatingPaths(test2["n"], test2["redEdges"], test2["blueEdges"]))