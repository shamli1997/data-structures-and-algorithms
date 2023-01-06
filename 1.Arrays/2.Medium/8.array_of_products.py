# Array of products
# write a function that takes an array and returns
# an array which contains product of every other number in the input array
# input: array= [5, 1, 4, 2]
# output: [8, 40, 10, 20]

# time: O(n^2) | space : O(n)
def bruitearrayOfProducts(array):
    # use 2 loops and calculate the product iff i != j
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct

    return products

# time: O(n) | space: O(n)


def optimizedarrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products
# 1. take an array of products initialized with 1
# 2. iterate over the array and insert the leftRunningProduct * array[i] in products array
# 3. iterate over the array in reverse order and insert rightRunningProduct * array[i]
# time: O(n) | space: O(n)


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


arr = [5, 1, 4, 2]
print(arrayOfProducts(arr))
