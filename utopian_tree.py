def utopian_tree(cycles):
    H = 1
    for i in range(1, cycles + 1):
        if i % 2 != 0:
            H *= 2
        else:
            H += 1

    return H
