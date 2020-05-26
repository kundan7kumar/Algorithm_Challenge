# Check elements in the array or not
# Two loops method.

def duplicate_array(num):
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                return num[i]
    return 0


num = [1, 2, 3, 6, 4, 2]
print(duplicate_array(num))


# Time Complexity:- O(n^2)
# Space Complexity:- O(1)

# using Sorting

def duplicate_array_sort(num):
    num.sort()
    for i in range(len(num)):
        if num[i] == num[i + 1]:
            return num[i]
    return 0


print(duplicate_array_sort(num))

# Time Complexity:- O(nlogn)
# Space Complexity:- O(1)

# Using Hashing

def duplicate_array_hash(num):

# 