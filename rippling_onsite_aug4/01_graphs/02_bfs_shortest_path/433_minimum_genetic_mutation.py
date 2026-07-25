"""Practice: 433. Minimum Genetic Mutation

Do not look up the solution yet.

One mutation changes exactly one character. Every intermediate gene must be
present in the bank. Return the minimum number of mutations, or -1.
"""

from collections import deque

def minMutation(startGene, endGene, bank):
    bank_set = set(bank)

    if endGene not in bank_set:
        return -1

    visited = set([startGene])
    queue = deque([(startGene, 0)])

    allowed_chars = ('A', 'C', 'G', 'T')

    while queue:
        node, mutations = queue.popleft()

        if node == endGene:
            return mutations


        

        for i in range(len(node)):
            gene_arr = list(node)
            for c in allowed_chars:
                gene_arr[i] = c
                candidate = "".join(gene_arr)
                if candidate in bank_set and candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, mutations + 1))



    return -1




# -------------------------------------------------
# Practice test cases
# -------------------------------------------------
start_one = "AACCGGTT"
end_one = "AACCGGTA"
bank_one = ["AACCGGTA"]
expected_one = 1

start_two = "AACCGGTT"
end_two = "AAACGGTA"
bank_two = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
expected_two = 2


# -------------------------------------------------
# Before coding, explain the problem
# -------------------------------------------------
# 1. What represents a node in this graph?
# 2. When are two genes connected by an edge?
# 3. Which possible mutations are valid?
# 4. Why is BFS appropriate?
# 5. What should one queue item store?
# 6. When should a gene be marked visited?
# 7. What should happen if end_gene is not in bank?
#
# After implementing your method, test it with:
# result_one = your_method_here(start_one, end_one, bank_one)
# result_two = your_method_here(start_two, end_two, bank_two)
#
# assert result_one == expected_one
# assert result_two == expected_two
