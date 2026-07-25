

def tarjans_algo(n, edges):

    # build adjacency list
    graph = {i: [] for i in range(n)}

    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)


    # initialize tracking structures
    discovery = [-1] * n
    low = [0] * number_of_nodes
    bridges = []

    time = [0]

    def dfs(node, parent):
        discovery[node] = time[0]
        
