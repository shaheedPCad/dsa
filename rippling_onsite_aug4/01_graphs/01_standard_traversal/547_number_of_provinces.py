# There are n cities. Some of them are connected, while some are not. If city
# a is connected directly with city b, and city b is connected directly with
# city c, then city a is connected indirectly with city c.

# A **province** is a group of directly or indirectly connected cities and no
# other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# ith city and the jth city are directly connected, and isConnected[i][j] = 0
# otherwise.

# Return *the total number of* ***provinces***.

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

def findCircleNum(isConnected):
    n = len(isConnected)
    provinces = 0

    visited = set()


    def dfs(city):
        visited.add(city)

        for nei in range(n):
            if isConnected[city][nei] == 1 and nei not in visited:
                dfs(nei)



    for city in range(n):
        if city not in visited:
            provinces += 1
            dfs(city)


    return provinces




# Test case 1
test1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
]
# Expected output: 2


# Test case 2
test2 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# Expected output: 3

print(findCircleNum(test2))


# Example usage after implementing the method:
# solution.findCircleNum(test1)
# solution.findCircleNum(test2)
