# Three Sum
# input : 
    # array : [12, 3, 1, 2, -6, 5, -8, 6]
    # target_sum = 0
# output :
    # [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# 1. Iterate over array from first ele to third last ele
# 2. iterate over array till second last ele
# 3. set left and right pointers
# 4. compare currentSum with targetSum and in/dec left/right pointers accordingly

# time : O(n^2) | space : O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets