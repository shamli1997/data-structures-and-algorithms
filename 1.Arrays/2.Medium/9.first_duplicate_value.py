# time: O(n^2) | space: O(1)
# 1.Iterate over array with 2 nested for loops
# 2.Compare the i and j elements if the match is found update the minIdx
# 3. return array[minIdx]
def firstDuplicateValue(array):
    minIdx = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minIdx = min(minIdx, j)

    if minIdx == len(array):
        return -1

    return array[minIdx]

# time: O(n) | space: O(n)
# 1. Iterate over an array if ele is already there in set return the ele otherwise add it into the set


def firstDuplicateValue(array):
    seen = set()
    for a in array:
        if a in seen:
            return a
        seen.add(a)

    return -1

# time : O(n) | space : O(1)
# 1.Iterate over an array check if array[absVal - 1] is negative. If yes then return otherwise make it negative
# 2.Here it is given in the question that the array contains ele ranging from 1 to n where n is the len of arr


def firstDuplicateValue(array):
    for a in array:
        absVal = abs(a)

        if array[absVal - 1] < 0:
            return absVal
        array[absVal - 1] *= -1
    return -1
