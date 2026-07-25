from collections import deque


def kahns_top_sort(nodes, edges):

    # construct adj_list and indegrees array
    adj_list = {i: [] for i in range(nodes)}
    indegrees = [0] * nodes


    for src, dest in edges:
        adj_list[src].append(dest)
        indegrees[dest] += 1


    # add nodes with indegree 0 to queue
    queue = deque()

    for i in range(nodes):
        if indegrees[i] == 0:
            queue.append(i)


    # process queue
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for nei in adj_list[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)


    if len(result) != nodes:
        return []


    return result
