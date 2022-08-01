# time : O(n) | space : O(n)
def spiralTraverse(array):
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1
    result = []

    while startRow <= endRow and startCol <= endCol:
        print("startRow: ", startRow)
        print("endRow: ",endRow)
        print("startCol: ",startCol)
        print("endCol: ", endCol)
        print("====Row===")
        for col in range(startCol, endCol + 1):
            print(f"array[{startRow}][{col}] : {array[startRow][col]}")
            result.append(array[startRow][col])

        print("====Col===")
        for row in range(startRow + 1, endRow + 1):
            print(f"array[{row}][{endCol}] : {array[row][endCol]}")
            result.append(array[row][endCol])

        print("====inner row====")
        for col in reversed(range(startCol, endCol)):
            # Handle the edge case when there's a single row
            # in the middle of the matrix. In this case, we don't
            # want to double count the values in this row,
            # which we've already counted in the first for loop above
            if startRow == endRow:
                break
            
            print(f"array[{endRow}][{col}] : {array[endRow][col]}")
            result.append(array[endRow][col])

        print("==========inner col=============")
        for row in reversed(range(startRow + 1, endRow)):
            # Handle the edge case when there's a single col
            # in the middle of the matrix. In this case, we don't
            # want to double count the values in this col,
            # which we've already counted in the second for loop above
            if startCol == endCol:
                break
            print(f"array[{row}][{startCol}] : {array[row][startCol]}")
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return result

# array = [[1,2,3,4],
# [10,11,12,5],
# [9,8,7,6]]

array = [[1, 2, 3],
[8,9,4],
[7,6,5]]
print(spiralTraverse(array))