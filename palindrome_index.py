def palindrome_index(s):
    if s == s[::-1]:
        return -1

    s = [x for x in s]
    j = len(s) - 1

    for i in range(len(s)):
        if s[i] != s[j]:
            del s[i]
            if s == s[::-1]:
                return i
            else:
                return j
        j -= 1


s = 'qawertrewq'

print(palindrome_index(s))
