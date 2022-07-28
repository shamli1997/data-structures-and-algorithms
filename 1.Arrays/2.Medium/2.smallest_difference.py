# Smallest Difference
# find a pair of numbers from 2 arrays whose difference is closest to 0
# input : 
    # arrayOne : [-1, 5, 10, 20, 28, 3]
    # arrayTwo : [26, 134, 135, 15, 17]
# output :
    # [28, 26]

# 1.sort both arrays
# 2.iterate through both arrays and compare the ele and calculate diff
# 3.update the current diff with smallest diff
# 4.return the smallestpair

# time : O(n log(n) + m log(m)) | space : O(1)
def smallestDifference(arrayOne, arrayTwo):
    # 1.sort both arrays
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0

    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        # if arr1 ele is smaller increment idxOne
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        # if arr2 ele is smaller increment idxTwo
        elif firstNum > secondNum:
            current = firstNum- secondNum 
            idxTwo += 1
        # both elements are same so diff is 0
        else:
            return [firstNum, secondNum]
        # update the smallest difference
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    
    return smallestPair