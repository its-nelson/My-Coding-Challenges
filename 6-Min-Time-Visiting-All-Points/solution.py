def minTimeToVisitAllPoints(points):
    """Gets the minimum time in seconds to visit all points in the given 
    order"""
    counter = 0
    x1, y1 = points.pop()

    while points:
        x2, y2 = points.pop()
        counter += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    return counter

# Example 1
print(f"Example 1\nOutput:\n{minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])}\n")

# Example 2
print(f"Example 2\nOutput:\n{minTimeToVisitAllPoints([[3,2],[-2,2]])}\n")