# 4. Two Sum (LeetCode #1)

**Link to Problem:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---
## My Approach and Thought Process

The core idea is to find two numbers in the array `nums` that sum up to the given `target`. A brute-force approach (checking every pair) would be O(n^2), which can be inefficient for larger inputs.

My solution uses a **Hash Map (Dictionary in Python)** to optimize the lookup process, bringing the time complexity down to O(n). Here's the detailed logic:

1.  **Initialize a Hash Map:** Create an empty hash map (e.g., `nums_hashmap`). This map will store numbers from the input array as keys and their corresponding indices as values.
2.  **Iterate Through the Array:** Loop through the `nums` array, processing each number `num` along with its index `i`.
3.  **Calculate the Complement:** For each `num`, determine the `num_needed` to reach the `target`. This is calculated as `target - num`.
4.  **Check in Hash Map:** Check if `num_needed` already exists as a key in the `nums_hashmap`.
    * **If `num_needed` is found:** This means we have found the two numbers that sum up to `target`. The current number `num` (at index `i`) and the number corresponding to `num_needed` (whose index is stored in `nums_hashmap[num_needed]`) are our answer. Return `[i, nums_hashmap[num_needed]]`.
    * **If `num_needed` is NOT found:** This means the current `num` is not part of a pair found so far. Add `num` and its index `i` to the `nums_hashmap` (i.e., `nums_hashmap[num] = i`). This makes `num` available for future lookups as a `num_needed` for subsequent elements in the array.

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * The solution involves a single pass through the `nums` array O(n).
    * Inside the loop, hash map operations (insertion and lookup) take an average time complexity of O(1).
    * Therefore, the total time complexity is O(n), proportional to the number of elements in the input array.