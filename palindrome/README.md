# Palindrome Problem

## Problem
Given a string `s`, return `True` if it is a palindrome, otherwise return `False`.

A palindrome reads the same forward and backward.

## Examples

- Input: `"madam"` → `True`
- Input: `"hello"` → `False`
- Input: `"racecar"` → `True`

---

## Solutions

### 1. Slicing
```python
def palindrome(s):
    return s == s[::-1]
```

### 2. Using reversed()

 ```python
def palindrome(s):
    return s == ''.join(reversed(s))
```
Time Complexity: O(n)
Space Complexity: O(n)

### 3. Two Pointers
```python
def palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```
Time Complexity: O(n)
Space Complexity: O(1)

## What I Learned

Different ways to solve the same problem
String manipulation in Python
Two pointers technique
Time and space complexity analysis

## Author

Zouhour Bellamine
