def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]

    best = 0
    worst = 0

    for i in scores:
        if i > highest_score:
            highest_score = i
            best += 1
        if lowest_score > i:
            lowest_score = i
            worst += 1
    return (best, worst)
