a = [3, 4]
b = [24, 48]

from functools import reduce

c = range(reduce(lambda x, y: x * y, a), min(b) + 1)
print(list(c))
l = set()
for i in c:
    for j in a:
        if i % j == 0:
            l.add(i)
print(l)
