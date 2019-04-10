def cut_the_sticks(arr):
    result = []
    while arr:
        minElement = min(arr)
        result.append(len(arr))
        for i in arr:
            if i == minElement:
                arr.remove(i)

        arr = [x - minElement for x in arr if x - minElement != 0]

    return result


arr = [1, 2, 3, 4, 3, 3, 2, 1]
result = cut_the_sticks(arr)

print('\n'.join(map(str, result)))
