# Union Find

## Must Know

Use Union Find when the problem is about grouping, merging, or connectivity.

Core operations:

- `find`: get representative/root
- path compression: make future finds faster
- `union`: merge two groups
- rank/size: attach smaller tree under bigger tree

## Drill Problems

- Accounts Merge
- Satisfiability of Equality Equations
- Lexicographically Smallest Equivalent String
- Similar String Groups, hard stretch

## Watch For

- Mapping real values like emails or strings to integer ids
- Grouping by root after all unions are complete
- Calling `find` again when building final groups
