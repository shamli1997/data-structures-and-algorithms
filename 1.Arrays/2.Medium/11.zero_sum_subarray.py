# zero sum subarray
# subarray where all the values add up to 0
# input: nums=[-5, -5, 2, 3, -2]
# output: True

# time: O(n) | space: O(n)
def zeroSumSubarray(nums):
    # zero sum sub array starting from index 0
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)

    return False
