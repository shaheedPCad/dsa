"""Closed-book template diagnostic.

Write each implementation from memory. For every section, be ready to explain:
- the invariant;
- why each data structure is appropriate;
- when nodes/items are marked visited or processed;
- time and auxiliary-space complexity;
- at least two edge cases.
"""


# 1. Graph BFS, including a disconnected graph.
from collections import deque
from collections import defaultdict
import heapq

def bfs(graph):
    visited = set()
    result = []

    for start in graph.keys():
        if start in visited:
            continue

        visited.add(start)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            result.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)


    return result


def bfs_connected(start, graph):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        
        if node in visited:
            continue

        result.append(node)
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)

    return result


# 2. Recursive and iterative graph DFS.

def dfs_recursive(node, visited, result, graph):
    visited.add(node)
    result.append(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs_recursive(nei, visited, result, graph)


    return result


def dfs_iterative(start, graph):
    stack = [start]
    visited = set()
    result = []


    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        for nei in graph[node]:
            if nei not in visited:
                stack.append(nei)

    return result



# 3. Grid DFS/BFS (four directions).
def numOfIslands(grid):
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        num_of_islands = 0

        def traverse(r, c):
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            traverse(r + 1, c)
            traverse(r - 1, c)
            traverse(r, c + 1)
            traverse(r, c - 1)


        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    num_of_islands += 1
                    traverse(r, c)

        return num_of_islands





# 4. Level-order traversal of a binary or N-ary tree.
# children is a list of TNode
class TNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

def levelOrder(root):
    if root is None:
        return []

    queue = deque([root])

    levels = []

    while queue:
        level_size = len(queue)
        level = []


        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.children:
                queue.extend(node.children)

        levels.append(level)


    return levels


# 5. Weighted-graph path search returning the accumulated product.
def calcEquation(equations, values, queries):

    # build graph
    graph = defaultdict(list)

    for i, (valA, valB) in enumerate(equations):
        graph[valA].append((valB, values[i]))
        graph[valB].append((valA, 1 / values[i]))

    def query(source, dest):
        if (source not in graph) or (dest not in graph):
            return -1.0

        queue = deque([(source, 1.0)])
        visited = set([source])
        
        while queue:
            node, product= queue.popleft()
            if node == dest:
                return product


            for nei, weight in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, product * weight))

        return -1.0


    answers = []

    for src, dest in queries:
        answers.append(query(src, dest))

    return answers





# 6. Kahn's topological sort with cycle detection.
def kahn_top_sort(nodes, edges):
    # build adj list and indegrees array
    adj_list = {i: [] for i in range(nodes)}
    indegrees = [0] * nodes

    for src, dest in edges:
        adj_list[src].append(dest)
        indegrees[dest] += 1


    # add nodes with indegree 0 to queue

    queue = deque()

    for i in range(nodes):
        if indegrees[i] == 0:
            queue.append(i)


    # process queue
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for nei in adj_list[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)


    if len(result) != nodes:
        return []

    return result



# 7. Union Find with path compression and union by rank/size.
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


    # union by rank
    def union(self, a, b):
        # get root of a and b
        rootA = self.find(a)
        rootB = self.find(b)

        # do nothing if both have same root
        if rootA == rootB:
            return False

        # attach smaller tree under bigger tree
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1


        return True



    # check if two nodes have same root
    def connected(self, a, b):
        return self.find(a) == self.find(b)




# 8. Min-heap Top K pattern.
def topKFrequent(nums, k):
    freq = {} # num : num of occurences

    # build freq dictionary
    for n in nums:
        freq[n] = freq.get(n, 0) + 1


    # build heap with (freq, num)
    heap = []

    for num, val in freq.items():
        heap.append((-val, num))


    heapq.heapify(heap)

    res = []

    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res



# median of two sorted arrays
def findMedianBaseLine(nums1, nums2):
    arr = sorted(nums1 + nums2)

    if len(arr) % 2 == 0:
        m1 = len(arr) // 2
        m2 = m1 - 1

        return float((arr[m1] + arr[m2]) / 2)

    return float(arr[len(arr) // 2])



# median of two sorted arrays optimals
def findMedianOfTwo(nums1, nums2):
    A = nums1
    B = nums2

    if len(A) > len(B):
        A, B = B, A



    l = 0
    r = len(A)
    total_size = len(A) + len(B)
    left_size = (total_size + 1) // 2



    while l <= r:

        cutA = (l + r) // 2
        cutB = left_size - cutA

        Aleft = A[cutA - 1] if cutA != 0 else float("-inf")
        Aright = A[cutA] if cutA != len(A) else float("inf")
        Bleft = B[cutB - 1] if cutB != 0 else float("-inf")
        Bright = B[cutB] if cutB != len(B) else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if total_size % 2 != 0 :
                return max(Aleft, Bleft)

            # if length is even
            left_middle = max(Aleft, Bleft)
            right_middle = min(Aright, Bright)
            return float((left_middle + right_middle) / 2)

        elif Aleft > Bright:
            r = cutA - 1

        elif Bleft > Aright:
            l = cutA + 1

    return







# 9. Merge two sorted linked lists.
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None


def mergeTwoSortedLists(list1, list2):

    dummy = Node()

    tail = dummy

    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next

        else:
            tail.next = list1
            list1 = list1.next
        tail = tail.next


    if list1:
        tail.next = list1
    
    elif list2:
        tail.next = list2

    return dummy.next



# decode string
def decodeString(s):
    
    stack = []

    # build stack
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])

        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr

            stack.pop()


            k = ""

            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * substr)

    return "".join(stack)




# 10. Merge intervals.
def merge(intervals):
    if not intervals:
        return []


    intervals.sort(key = lambda x: x[0])

    res = [intervals[0]]


    for curr_inter in intervals[1:]:
        last_inter = res[-1]

        if last_inter[1] >= curr_inter[0]:
            res[-1][1] = curr_inter[1] if curr_inter[1] >= last_inter[1] else last_inter[1]

        else:
            res.append(curr_inter)

    return res




# 11. Binary search with explicit boundary semantics.
def bin_search(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target <  nums[m]:
            r = m - 1

        elif target > nums[m]:
            l = m + 1
        else:
            return m

    return -1 


# 12. Stack-based nested-string parsing.


# 13. Sliding window with a set or last-seen index map.


# 14. LRU Cache using a hashmap and doubly linked list.

class DLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key : node
        self.head = DLNode(0, 0)
        self.tail = DLNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        # return -1 if key not int cache
        if key not in self.cache:
            return -1

        # get node from cache
        node = self.cache[key]

        # remove node from linked list
        self.remove(node)

        # add node to front of linked list
        self.insert(node)

        return node.val


        

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            return

        new_node = DLNode(key, value)

        if len(self.cache) == self.capacity:
            # remove lru node
            lru_node = self.tail.prev
            self.remove(lru_node)

            # delete entry from cache
            del self.cache[lru_node.key]

        # add new node to cache
        self.cache[key] = new_node
        self.insert(new_node)
        return


    def insert(self, node):
        after = self.head.next
        self.head.next = node
        node.prev = self.head
        after.prev = node
        node.next = after


    def remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before







