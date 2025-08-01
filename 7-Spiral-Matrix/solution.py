def spiralOrder(matrix):
    """Returns all the elements of the matrix in spiral order"""
    ret = []
    while matrix:
        ret.extend(matrix.pop(0))
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret

# Example 1
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

# Example 2
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))