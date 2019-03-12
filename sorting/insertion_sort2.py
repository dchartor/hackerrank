arr = [9, 8, 6, 7, 3, 5, 4, 1, 2]
tmpArr = []
for i in range(1, len(arr)):

    if arr[i] < arr[i - 1]:
        tmp = arr.pop(i)
        tmpArr.append(arr[i - 1])
        for i in tmpArr:
            if tmp < i:
                ins = i
        print(tmpArr)
        arr.insert(arr.index(ins), tmp)
        #print(*arr, sep=' ')
    #else:
        #print(*arr, sep=' ')
