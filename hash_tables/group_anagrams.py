# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################




def group_anagrams(strs):


    freq = {} # "sorted_string" : [anagrams]

    for s in strs:
        sorted_s = ''.join(sorted(s))

        if sorted_s in freq:
            freq[sorted_s].append(s)
        else:
            freq[sorted_s] = [s]


    res = []
    for value in freq.values():
        res.append(value)


    return res








print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""