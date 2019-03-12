def repeatedString(string, n):
    return (string.count('a') * (n // len(string)) + string[:n % len(string)].count('a'))
