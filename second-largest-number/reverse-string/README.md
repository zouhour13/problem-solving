# Reverse String

## Problem
Write a function that reverses a given string.

## Example

Input:
hello

Output:
olleh

## Solutions Included

1. Using loop + indexing
2. Using slicing
3. Using reversed() + join()

## Time Complexity

- Loop + indexing: O(n²) because string concatenation
- Slicing: O(n)
- reversed() + join(): O(n)

## Best Solution

Using slicing:

```python
s[::-1]