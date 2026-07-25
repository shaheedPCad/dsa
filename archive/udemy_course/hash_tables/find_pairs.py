

# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################


def find_pairs(arr1, arr2, target):

    arr1_set = set(arr1)


    res = []


    for n in arr2:
        diff = target - n

        if diff in arr1_set:

            res.append((diff, n))

            arr1_set.remove(diff)


    return res



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""