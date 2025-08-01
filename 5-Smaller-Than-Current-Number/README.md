# 5. How Many Numbers Are Smaller Than the Current Number (LeetCode #1365)

**Link to Problem:** [https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

## Problem Statement
Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j`'s such that `j != i` and `nums[j] < nums[i]`.
Return the answer in an array.

---
## Sample Output

### Example 1
```
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
```

### Example 2
```
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Explanation:
For nums[0]=6 there exist two smaller numbers than it (4 and 5). 
For nums[1]=5 there exist one smaller number than it (4).
For nums[2]=4 does not exist any smaller number than it. 
For nums[3]=8 there exist three smaller numbers than it (4, 5, and 6). 
```

### Example 3
```
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
Explanation:
Since all the elements in nums are the same (7), no other number in 
the array is smaller than it.
```

---
## My Approach and Thought Process

The problem asks us to count, for each number in the input array `nums`, how many other numbers in the same array are strictly smaller than it.

My solution combines **sorting** and a **hash map** (dictionary in Python). Here is the logic:

1.  **Sort the Array:** First, create a sorted copy of the input `nums` array, called `sorted_nums`. Sorting takes O(n log n) time.
2.  **Populate a Hash Map with Counts:** Iterate through the `sorted_nums` array. For each unique number `num` encountered, store its index `i` in a hash map. The key will be `num`, and the value will be `i`.
    * **Why the index `i`?** Because in a sorted array, the index of an element directly tells you how many elements are strictly smaller than it *if all elements were unique*. For duplicate numbers, we only store the index of its *first* occurrence. This ensures that for a number `X`, `hashmap[X]` gives the count of elements strictly smaller than `X` in the original array.
3.  **Construct the Result Array:** Finally, iterate through the *original* `nums` array. For each number `num` in the original array, look up its corresponding count in the `hashmap` (`hashmap[num]`) and append this count to a `smaller_nums` result list.
4.  **Return the Result:** The `smaller_nums` list will contain the desired counts for each number in the original `nums` array.

---
## Complexity Analysis

* **Time Complexity: O(n log n)**
    * Sorting the `nums` array takes O(n log n) time.
    * Iterating through the sorted array to populate the hash map takes O(n) time, as hash map insertions are O(1) on average.
    * Iterating through the original `nums` array to build the result list takes O(n) time, as hash map lookups are O(1) on average.
    * The dominant factor is the sorting step, so the overall time complexity is O(n log n).