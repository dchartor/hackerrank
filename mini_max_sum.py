def miniMaxSum(arr):
    arr.sort()
    max = arr[1:]
    min = arr[:-1]

    print(sum(min), sum(max))
