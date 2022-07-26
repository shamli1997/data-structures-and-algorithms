# Validate Subsequence
# subsequence is set of array in same order as they appear in array
# input : 
    # array : [5, 1, 22, 25, 6, -1, 8, 10]
    # sequence : [1, 6, -1, 10]
# output :
    # true

# time : o(n) | space : o(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
        
    return seqIdx == len(sequence)