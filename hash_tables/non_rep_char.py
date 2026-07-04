# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################

def first_non_repeating_char(sequence):

    freq = {}  # char : [index, freq]

    for s in  sequence:
        freq[s] = freq.get(s, 0)  + 1


    for key, value in freq.items():
        if value == 1:
            return key
        
    return












print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""