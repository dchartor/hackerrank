def findDigits(n):
    arr = [int(x) for x in str(n) if x != '0']
    return len([x for x in arr if n % x == 0])
