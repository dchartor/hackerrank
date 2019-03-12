def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                res += 1
    return res
