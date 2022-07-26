# Two Sum
# input : 
    # array : [3, 5, -4, 8, 11, 1, -1, 6]
    # target_sum = 10
# output :
    # [-1, 11]

# time : o(n^2) | space : o(n)
def twoNumberSumBrute(array, targetSum):
	for i in range(0,len(array)-1):
		firstNum = array[i]
		for j in range(i+1,len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return[firstNum,secondNum]
			
	return []

# time : o(n) | space : o(n)
def twoNumberSumOptimized(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return[num,potentialMatch]
        else:
            nums[num]=True
    return []

# time : o(n log n) | space : o(n)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

