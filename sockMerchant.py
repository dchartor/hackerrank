def sockMerchant(n, ar):
    uniq = set(ar)
    pairs = 0

    for i in uniq:
        num = ar.count(i)
        pairs += num // 2
    return pairs
