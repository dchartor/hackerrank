def diagonalDifference(arr):
    return abs(sum([arr[x][x] for x in range(len(arr))]) - sum([arr[x][len(arr)-x-1] for x in range(len(arr))]))
