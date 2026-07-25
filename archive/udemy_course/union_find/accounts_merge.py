
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n


    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]


    def union(self, a, b):
        # get root of both nodes
        rootA = self.find(a)
        rootB = self.find(b)

        # if both roots are equal do nothing
        if rootA == rootB:
            return False

        # place smaller tree under larger
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootB] > self.rank[rootA]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)






def accounts_to_merge(accounts):
    email_to_index = {} # email : index
    email_to_name = {} # email : name


    # create mappings
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_index:
                email_to_index[email] = len(email_to_index)

        email_to_name[email] = name


    # initialize union find with email as nodes
    uf = UnionFind(len(email_to_index))


    for account in accounts:
        first_email = account[1]

        for email in account[2:]:
            uf.union(email_to_index[first_email], email_to_index[email])



    groups = defaultdict(list)

    # find root of each email add email to same group
    for email, index in email_to_index.items():
        root = uf.find(index)
        groups[root].append(email)


    result = []


    # iterate through groups and assign each group its name and construct
    #   result array
    for root, emails in groups.items():
        sorted_emails = sorted(emails)

        name = email_to_name[sorted_emails[0]]

        result.append([name] + sorted_emails)

    return result



accounts = [
    ["John", "a@gmail.com", "b@gmail.com"],
    ["John", "c@gmail.com", "b@gmail.com"],
    ["Mary", "d@gmail.com"]
]


accounts_to_merge(accounts)




