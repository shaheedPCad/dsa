
# dfs recursive
def adj(node, adj, visited):
    if node in visited:
        return

    visited.add(node)


    for nei in adj[node]:
        dfs(nei, adj, visited)





# dfs iterative
def dfs


