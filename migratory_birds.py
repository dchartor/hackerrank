def migratoryBirds(arr):
    dic = dict.fromkeys(set(arr), 0)

    for i in arr:
        dic[i] += 1

    return(list(dic.keys())[list(dic.values()).index(max(dic.values()))])
