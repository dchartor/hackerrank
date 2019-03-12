def pickingNumbers(arr):
    arr.sort()
    count = 1
    ls = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) <= 1:
                count += 1
            else:
                ls.append(count)
                count = 1
                break

    if ls:
        return max(ls)
    else:
        return len(arr)
