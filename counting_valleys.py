def countingValleys(n, s):
    level = 0
    valleys = 0

    for i in s:
        if i == 'D':
            level -= 1
            if level == -1:
                valleys += 1
        if i == 'U':
            level += 1

    return valleys
