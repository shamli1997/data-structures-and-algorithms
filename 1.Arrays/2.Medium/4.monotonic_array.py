# Monotonic array [ele from L to R are entirely non-increasing or non decreasing]
# empty arr or arr with one ele is monotonic arr
# input : 
    # array : [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# output :
    # True

# 1. assume that array is both entirely non-dec and non-inc.
# 2. as you iterate through each ele check if you can invalidate any or both of your assumptions.

# time : O(n) | space : O(1)
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False

    return isNonIncreasing or isNonDecreasing