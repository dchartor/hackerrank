def beautifulDays(i, j, k):
    count = 0
    for i in range(i, j+1):
        if (i - int(''.join(list(reversed(str(i)))))) % k == 0:
            count += 1
    return count
