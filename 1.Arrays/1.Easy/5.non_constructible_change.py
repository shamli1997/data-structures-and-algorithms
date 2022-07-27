# write a function that returns minimum amount of change that cannot be created
# input : 
    # coins : [5, 7, 1, 1, 2, 3, 22]
# output :
    # 20

# 1. Sort the input array
# 2. Loop through 1 coin at a time
# 3. keep track of how much change we currently create
# 4. check for some coin that we add that is greater than currentChange + 1
# 5. return currentChange + 1

# time : O(nlogn) | space : O(1)
def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
    return currentChange + 1