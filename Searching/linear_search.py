# Unordered Linear Search
def linear_search(num, val):
    for i in range(len(num)):
        if num[i] == val:
            return i
    return 0


num = [2, 1, 5, 3, 8, 7]
print(linear_search(num, 1))

# Time Complexity:- O(n)
# Space Complexity:- O(1)