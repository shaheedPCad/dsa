# Topological Sort

## Must Know

Use topological sort for dependency ordering.

The core idea:

- edge from prerequisite to dependent item
- indegree counts unmet prerequisites
- queue starts with indegree 0 nodes
- if result length is smaller than node count, there is a cycle

## Drill Problems

- Course Schedule
- Course Schedule II
- Alien Dictionary, hard stretch
- Sort Items by Groups Respecting Dependencies, hard stretch

## Interview Explanation

Nodes with indegree 0 are safe to process because they have no remaining
requirements. When we process one, we remove its outgoing edges and reduce the
indegree of its neighbors.
