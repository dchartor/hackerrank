def insertionSort1(n, arr):
    store = arr[-1]
    i = n - 2

    while (store < arr[i]) and i >= 0:
        if store < arr[i]:
            arr[i + 1] = arr[i]
            print(' '.join(str(x) for x in arr))
            i -= 1

    arr[i + 1] = store
    print(' '.join(str(x) for x in arr))
