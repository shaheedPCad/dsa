# BFS Shortest Path

## Must Know

BFS gives shortest path only when each edge has equal cost.

Use BFS when the problem asks for:

- minimum number of moves
- nearest exit
- shortest transformation
- shortest path in binary matrix
- level-by-level spread

## Drill Problems

- Nearest Exit from Entrance in Maze
- Minimum Genetic Mutation
- 01 Matrix
- Shortest Path in Binary Matrix
- Shortest Bridge
- Word Ladder, hard stretch

## Pitfalls

- Mark visited when enqueuing, not after popping, to avoid duplicates
- Track distance by queue levels or by storing distance in the queue
- For grids, validate boundaries before indexing
