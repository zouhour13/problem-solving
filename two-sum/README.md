# 🧩 Two Sum

## 📌 Problem Statement

Given an array of integers and a target value, the goal is to find two different numbers in the array such that their sum equals the target.  
You must return the indices of these two numbers.

---

## 🚀 Approach

### 🧠 Optimized Approach (Hash Map)

Instead of checking every possible pair of numbers (which is slow), we use a hash map to store numbers we have already seen.

For each number in the array:
- We compute the difference between the target and the current number.
- We check if this difference already exists in our stored values.
- If it exists, it means we have found two numbers that add up to the target.
- If it does not exist, we store the current number and continue.

---

## ⏱ Complexity

- Time Complexity: O(n) because we traverse the array once  
- Space Complexity: O(n) because we store elements in a hash map  

---

## 🧠 Key Idea

The main idea is to avoid repeated comparisons by using extra memory to store previously seen values, which allows fast lookup.

---

## 🏆 What I learned

- How hash maps can reduce time complexity significantly  
- How to trade space for speed in optimization problems  
- How to recognize pair-sum patterns in arrays  
