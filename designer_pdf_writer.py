def designerPdfViewer(arr, word):
    from string import ascii_lowercase

    dic = dict(zip(ascii_lowercase, arr))
    for i in word:
        qwe = [dic[i] for i in word]

    return max(qwe) * len(word)
