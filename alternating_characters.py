def alternating_characters(s):
    count = 0
    for i in range(0, len(s) - 1):
        init = s[i]
        if init == s[i + 1]:
            count += 1
    return count
