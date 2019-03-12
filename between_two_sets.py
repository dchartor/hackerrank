a = [2, 3, 6]
b = [16, 32, 96]


def fact(x, y):
    mass = []
    for i in range(x, y+1):
        if i % x == 0:
            mass.append(i)
    return mass


print(list(map(lambda x: fact(x, min(b)), a)))
a = [fact(x, min(b)) for x in a]

asd = []
for i in range(-1, len(a) - 1):
    print(set(a[i]) | set(a[i + 1]))
