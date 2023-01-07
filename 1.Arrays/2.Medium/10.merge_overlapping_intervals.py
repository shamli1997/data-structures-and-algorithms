# Merge Overlapping intervals
# Input: intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# Output: [[1, 2], [3, 8], [9, 10]]

#  1. Iterate over the sortedarray
#  2. compare if startEle of currInt >= startEle of nextInt
# Yes: change the endEle of CurrEle to largest val
# No: take nextInt and append it to the mergedInt

# time: O(nlogn) | space: O(n)
def mergeOverlappingIntervals(intervals):
    # sort the array by 1st ele
    sortedIntervals = sorted(intervals, key=lambda a: a[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(nextIntervalEnd, currentIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))
