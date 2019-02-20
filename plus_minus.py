def plusMinus(arr):
    positive = len([x for x in arr if x > 0]) / len(arr)
    negative = len([x for x in arr if x < 0]) / len(arr)
    zero = len([x for x in arr if x == 0]) / len(arr)

    print(positive, negative, zero, sep='\n')
