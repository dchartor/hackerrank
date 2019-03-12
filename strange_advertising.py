def viralAdvertising(n):
    cumulative, liked = 0, 0
    shared = 5

    for i in range(n):
        liked = shared // 2
        shared = liked * 3
        cumulative += liked

    return cumulative
