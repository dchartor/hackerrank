def sherlock(a, b):
    import math
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count
