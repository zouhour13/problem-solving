
---

# 🐍 solution.py

```python
# Solution 1: Loop + Indexing
def reverse_string_loop(s):
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


# Solution 2: Slicing
def reverse_string_slice(s):
    return s[::-1]


# Solution 3: reversed() + join()
def reverse_string_reversed(s):
    return ''.join(reversed(s))


# Test
word = "hello"

print("Loop:", reverse_string_loop(word))
print("Slice:", reverse_string_slice(word))
print("Reversed:", reverse_string_reversed(word))