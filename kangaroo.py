def kangaroo(x1, v1, x2, v2):
    while True:
        if v2 >= v1:
            return 'NO'
        else:
            x1 += v1
            x2 += v2
            if x1 > x2:
                return 'NO'
            elif x1 == x2:
                return 'YES'
