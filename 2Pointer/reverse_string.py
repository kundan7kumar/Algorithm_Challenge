# Write a function that reverses a string. The input string is given as an array of characters char[].
# Method I: Using Python Inbuilt functionality:

def reverse_string(strii):
    return strii[::-1]


print(reverse_string(["s", "w", "a", "t", "i"]))
print(reverse_string(["H", "a", "n", "n", "a", "h"]))


# Method II: Using python reverse function

def reverse_string1(s):
    return list(reversed(s))


print(reverse_string1(["h", "e", "l", "l", "o"]))
print(reverse_string1(["H", "a", "n", "n", "a", "h"]))


# Method III: Using Recursion, In place, O(N) Space
def reverse_string2(rstr):
    def recur_str(left, right):
        if left < right:
            rstr[left], rstr[right] = rstr[right], rstr[left]
            recur_str(left + 1, right - 1)

        recur_str(0, len(rstr) - 1)

    return rstr


print(reverse_string2(["h", "e", "l", "l", "o"]))
print(reverse_string2(["H", "a", "n", "n", "a", "h"]))


# Method IV: Using two pointer

def reverse_string3(rs):
    left, right = 0, len(rs) - 1
    while left < right:
        rs[left], rs[right] = rs[right], rs[left]
        left, right = left + 1, right - 1
    return rs


print(reverse_string3(["h", "e", "l", "l", "o"]))
print(reverse_string3(["H", "a", "n", "n", "a", "h"]))

## Complexity Analysis
# Time complexity : O(N)^2 to swap N/2 element.
# Space complexity : O(1)

