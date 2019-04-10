def acmTeam(topic):
    highest = -1
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            count = 0
            for y in range(len(topic[i])):
                if (topic[i][y] == '1' or topic[j][y] == '1'):
                    count += 1
            if count > highest:
                highest = count
                bestTeam = 1
            elif count == highest:
                bestTeam += 1

    return highest, bestTeam
