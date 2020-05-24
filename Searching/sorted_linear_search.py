def sorted_linear_search(num, val):
    for i in range(len(num)):
        if num[i] == val:
            return i
        elif num[i] > val:
            return 0
    return "Num not in array"


num = [1, 2, 3, 4, 5, 6]
print(sorted_linear_search(num, 7))

# Time Complexity:- O(n)
# Space Complexity:- O(1)
