s = 'dkhc'
s1 = list(s)

for i in range(len(s) - 1, -1, -1):
    if s[i] > s [i - 1]:
        s1[i], s1[i - 1] = s1[i - 1], s1[i]
        s1 = ''.join(s1)
        if s < s1:
            break
        elif s1 == s:
            s1 = 'no answer'
    # else:
    #     s = 'no answer'
    #     break
#
print(s1)
#print('lmon' > 'lmon')
# s = 'lmno'
# s = s.replace('l', 'asd')
print('dkhc' > 'kdhc')
