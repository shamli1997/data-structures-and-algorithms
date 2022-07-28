# Move to the End
# write a function that moves all the instances of the given integer at the end of the array
# no need to maintain order of other integers
# input : 
    # arrayOne : [2, 1, 2, 2, 2, 3, 4, 2]
    # toMove : 2
# output :
    # [1, 3, 4, 2, 2, 2, 2, 2]

# 1.set 2 ptrs at start and end of arr
# 2.move right ptr inwards so long as it points to int toMove
# 3.move left ptr inwards so long as it doesn't point to int toMove
# 4.when both ptrs are not moving swap their values inplace

# time : O(n) | space : O(1)
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array