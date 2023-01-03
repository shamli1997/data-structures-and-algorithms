# Longest Peak: Find length of the longest peak
# Input :
    # array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# output :
    # 6

# 1.Iterate over array till len(arr) - 1 because peak might be at second last ele
# 2.find the peak ele by comparing it with its left and right adjecent ele
# 3.If it is not a peak then just inc i and continue
# 4.If it is a peak find the len of that peak by iterating the array on left and right
    # leftIdx and rightIdx are inc and dec by 2 bcz we've already considered the adj ele of i
# 5.compare the peaklength and return longest peak

# time : O(n^2) | space : O(n)
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))