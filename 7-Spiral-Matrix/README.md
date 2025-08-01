# 7. Spiral Matrix (LeetCode #54)

**Link to Problem:** [https://leetcode.com/problems/spiral-matrix/](https://leetcode.com/problems/spiral-matrix/)

---
## Problem Statement
Given an `m x n` matrix, return all elements of the `matrix` in spiral order.

---
## Sample Output

### Example 1
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

---
## My Approach and Thought Process
This problem requires traversing a 2D matrix in a spiral pattern. My solution simulates this by "peeling" away the outer layer of the matrix in each iteration of a loop.

The process continues until the matrix is empty:
1.  **Traverse the Top Row:** I first take the entire top row (`matrix.pop(0)`) and extend the result list with its elements. This removes the top layer.
2.  **Traverse the Right Column:** If the matrix is not empty, I iterate through the remaining rows and pop the last element from each (`row.pop()`). This effectively removes the rightmost column.
3.  **Traverse the Bottom Row:** If the matrix still has rows, I pop the new bottom row. Since this row needs to be read from right to left, I reverse it (`[::-1]`) before extending the result list.
4.  **Traverse the Left Column:** Finally, if the matrix is still valid, I iterate through the remaining rows in reverse order (`matrix[::-1]`) and pop the first element of each (`row.pop(0)`). This removes the leftmost column.

The loop continues, with each step shrinking the matrix, until there are no more elements left.

---
## Complexity Analysis

* **Time Complexity: O(m * n)**
    * Every element in the `m x n` matrix is visited exactly once.
