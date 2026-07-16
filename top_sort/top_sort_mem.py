


def kahns_top_sort(nodes, edges):

    # build adjacency list and indegrees array
    adj_list = {i: [] for i in range(nodes)}