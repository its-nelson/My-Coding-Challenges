# 8. Number of Islands (LeetCode #200)

**Link to Problem:** [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

---
## Problem Statement
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---
## Sample Output

### Example 1
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

---
## My Approach and Thought Process
This problem can be modeled as finding the number of connected components in a graph. Each `'1'` is a node, and adjacent `'1'`s have an edge between them. My strategy is to iterate through every cell of the grid and, upon finding a piece of land (`'1'`) that I haven't visited yet, I initiate a **Breadth-First Search (BFS)** to find all connected parts of that same island.

The main logic is as follows:
1.  Initialize an `island counter` to zero and a `visited` set to keep track of cells I've already explored.
2.  Iterate through each cell (`r`, `c`) of the grid.
3.  If the current cell is land (`grid[r][c] == "1"`) and has not been visited, I have discovered a new island. I then:
    * Increment the `island counter`.
    * Call a `bfs` helper function starting from this cell to find and mark all parts of this island as visited.

**BFS Helper Function (`bfs`):**
The purpose of the BFS is to "sink" the entire island by visiting all its connected land parts.
1.  A `search_queue` (using `collections.deque`) is created to manage the cells to visit.
2.  The starting cell (`r`, `c`) is added to the queue and the `visited` set.
3.  While the queue is not empty, a cell is removed, and its four neighbors (up, down, left, right) are checked.
4.  If a neighbor is within the grid boundaries, is also land (`'1'`), and has not been visited, it gets added to both the queue and the `visited` set.

This process ensures that once we find one piece of an island, the BFS completely explores it, and we will not count any part of it as a new island again.

---
## Complexity Analysis

* **Time Complexity: O(m * n)**
    * Every cell in the `m x n` grid is visited exactly once.
