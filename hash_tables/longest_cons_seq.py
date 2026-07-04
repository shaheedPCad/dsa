# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################


def longest_consecutive_sequence(nums):

    nums_set = set(nums)

    longest = 0
    curr = 0
    for n in nums:
        while n + curr in nums_set:
            curr = curr + 1
            longest = max(longest, curr)


    return longest










# [1, 2, 3, 4, 100, 200]
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""