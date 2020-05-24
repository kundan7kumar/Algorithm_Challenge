# Iterative solution
def binary_search(num, val):
    low = 0
    high = len(num) - 1
    while low <= high:
        mid = (low + high) // 2
        if num[mid] > val:
            high = mid - 1

        elif num[mid] < val:
            low = mid + 1

        else:
            return mid

    return 0


# Time Complexity:- O(log(n))
# Space Complexity:- O(1)

num = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(num, 7))

# Recursive Solution
