
from collections import deque


# bfs on trees
def bfs(root):

    queue = deque()
    result = []

    queue.append(root)

    while queue:
        node = queue.popleft()
        result.append(node)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


    return result



# bfs on a graph
def bfs_graph(start, graph):
    visited = set()
    visited.add(start)

    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)





# bfs by level
def bfs_levels(start, graph):
    queue = deque()
    result = []

    while queue:
        level_size = len(queue)
        level = []


        for _ in range(level_size):
            node = queue.popleft()
            level.append(node)
            















