from collections import deque




def dfs_recursive(node, visited, graph):
    visited.add(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited, graph)


def dfs_iter(start, graph):
    visited = set()
    stack = [start]

    while queue:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                stack.append(nei)



def bfs(start, graph):
    visited = set([start])
    queue = deque([start])
    result = []


    while queue:
        node = queue.popleft()
        result.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)


    return result