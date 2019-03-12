def angry_professor(k, a):
    a = len(list(filter(lambda x: x <= 0, k)))
    if a >= k:
        return 'NO'
    else:
        return 'YES'
