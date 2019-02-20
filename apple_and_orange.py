def countApplesAndOranges(s, t, a, b, apples, oranges):
    house = range(s, t + 1)
    apples = [x + a for x in apples]
    oranges = [x + b for x in oranges]

    print(len([x for x in apples if x in house]), len([x for x in oranges if x in house]), sep='\n')
