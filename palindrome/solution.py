# Palindrome Problem - 3 Solutions


# -------------------------------------------------
# Solution 1: Slicing
# -------------------------------------------------
def palindrome_slicing(s):
    return s == s[::-1]


# -------------------------------------------------
# Solution 2: reversed()
# -------------------------------------------------
def palindrome_reversed(s):
    reverse_string = ''.join(reversed(s))
    return s == reverse_string


# -------------------------------------------------
# Solution 3: Two Pointers
# -------------------------------------------------
def palindrome_two_pointers(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# -------------------------------------------------
# Examples
# -------------------------------------------------
print(palindrome_slicing("madam"))        # True
print(palindrome_reversed("racecar"))     # True
print(palindrome_two_pointers("hello"))   # False