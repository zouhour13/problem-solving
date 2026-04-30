# Valid Parentheses

## Problem
Given a string containing (), {}, [] determine if it is valid.

## Approach
- Use a stack
- Push opening brackets
- On closing:
  - check match
  - pop if correct

## Example
Input: (){()}
Output: True

## Complexity
- Time: O(n)
- Space: O(n)