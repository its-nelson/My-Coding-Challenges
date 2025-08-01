# 6. Minimum Time Visiting All Points (LeetCode #1266)

**Link to Problem:** [https://leetcode.com/problems/minimum-time-visiting-all-points/](https://leetcode.com/problems/minimum-time-visiting-all-points/)

## Problem Statement
On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`. Return the minimum time in seconds to visit all the points in the order given by `points`.
You can move according to these rules:
In 1 second, you can either:
* move vertically by one unit,
* move horizontally by one unit, or
* move diagonally `sqrt(2)` units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

---
## Sample Output

### Example 1
```
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: 
Optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```

### Example 2
```
Input: points = [[3,2],[-2,2]]
Output: 5
Optimal path is [3,2] -> [2,2] -> [1,2] -> [0,2] -> [-1,2] -> [-2,2]  
Time from [3,2] to [-2,2] = 5 seconds 
Total time = 5 seconds
```

---
## My Approach and Thought Process

The problem asks for the minimum time to travel between a sequence of points on a 2D plane, with specific rules for movement: horizontal, vertical, and diagonal moves all take 1 second. The key to minimizing time between any two points is to utilize diagonal moves as much as possible, as they simultaneously cover both horizontal and vertical distance.

Let's consider two consecutive points, `P1(x1, y1)` and `P2(x2, y2)`.

1.  **Calculate Differences:** Determine the absolute horizontal distance `dx = |x2 - x1|` and the absolute vertical distance `dy = |y2 - y1|`.
2.  **Optimal Movement Strategy:**
    * The total time to move from `P1` to `P2` is `max(dx, dy)` which is known as the Chebyshev distance / Chessboard distance.

My solution uses this insight:

1.  **Initialize `counter`:** A counter is initialized to 0 to accumulate the time.
2.  **Iterate Through Points (Reverse Order):** The solution processes the `points` list by repeatedly `pop()`ing elements from the end. This effectively processes pairs of adjacent points from the end of the original sequence towards the beginning (e.g., from `points[n-1]` to `points[n-2]`, then from `points[n-2]` to `points[n-3]`, and so on).
3.  **Calculate Time for Each Segment:** In each iteration, it takes two consecutive points from the (remaining) list, calculates the `max(abs(y2 - y1), abs(x2 - x1))` between them, and adds this to `counter`.
4.  **Return `counter`:** Once all point segments have been processed, the accumulated `counter` is returned.

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * The solution iterates through the `points` array essentially once (each point is `pop()`ed a constant number of times).
    * Basic arithmetic operations (`abs`, `max`, addition) and list `pop()` operations are O(1).
    * Therefore, the total time complexity is O(n) with respect to the number of points.
