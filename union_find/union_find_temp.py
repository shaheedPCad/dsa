

class UnionFind:

    # initialize parent and rank arrays
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n



    # find root with path compression
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]


    # union two nodes
    def union(self, a, b): 

        # get root of both nodes
        rootA = self.find(a)
        rootB = self.find(b)

        # if both roots are same do nothing
        if rootA == rootB:
            return False


        # otherwise attach smaller tree to larger tree
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA

        elif self.rank[rootB] > self.rank[rootA]:
            self.parent[rootA] = rootB

        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        return True


    # check if two nodes have same root
    def connected(self, a, b):
        return self.find(a) == self.find(b)


