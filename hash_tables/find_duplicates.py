


def find_duplicates(nums):
    freq = {}
    res = []



    for n in nums:
        freq[n] = freq.get(n, 0) + 1


    for key, value in freq.items():
        if value > 1:
            res.append(key)

    return res





nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(find_duplicates(nums))