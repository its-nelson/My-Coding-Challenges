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