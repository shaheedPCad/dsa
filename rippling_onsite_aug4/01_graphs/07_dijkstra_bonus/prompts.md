# Dijkstra Bonus

This is lower priority than BFS, DFS, matrix graphs, topo, and Union Find.

Know the concept:

- min-heap stores best known distance candidates
- pop the smallest current distance
- skip stale heap entries
- relax neighbors

Use it when:

- graph is weighted
- edge weights are non-negative
- question asks shortest/minimum cost path

Do not overinvest here unless the earlier graph buckets feel solid.
