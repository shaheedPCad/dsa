# WRITE ITEM_IN_COMMON FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################

def item_in_common(list1, list2):
    list1_dict = {}
    
    for n in list1:
        list1_dict[n] = True
    
    for n in list2:
        if list1_dict.get(n) is True:
            return True
    
    return False




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""