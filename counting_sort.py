def counting_sort(arr):
    result = [0 for x in range(len(arr))]

    for i in arr:
        result[i] += 1

    return result


arr = [1, 1, 3, 2, 1]

print(counting_sort(arr))
