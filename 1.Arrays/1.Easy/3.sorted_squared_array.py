# Sorted Squared Array [input array is sorted in ascending order]
# input : 
    # array : [-9, -6, -2, 1, 2, 3, 4, 7]
# output :
    # [1, 4, 9, 16, 36, 49, 81]

# 1. Create new arr and append the squares
# 2. Sort the new array
# time : O(nlogn) | space : O(1)
def sortedSquaredArray(array):
    sqrArr = []
    for a in array:
        sqrArr.append(a*a)

    sqrArr.sort()
    return sqrArr

# 1.Initialize two pointers start and end
# 2.Compare absolute values and add the squares to array and inc/dec start/end ptrs
# time : O(n) | space : O(1)
def sortedSquaredArray(array):
    sqrArr = [0 for _ in array]
    smallIdx = 0
    largeIdx = len(array) - 1
    for i in reversed(range(len(array))):
        smallVal = array[smallIdx]
        largeVal = array[largeIdx]
        if abs(smallVal) > abs(largeVal):
            sqrArr[i] = smallVal * smallVal
            smallIdx +=  1
        else:
            sqrArr[i] = largeVal * largeVal
            largeIdx -=  1
    return sqrArr