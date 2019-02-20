def compareTriplets(a, b):
    l = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            l[0] += 1
        elif a[i] < b[i]:
            l[1] += 1
        else:
            continue
    return l
