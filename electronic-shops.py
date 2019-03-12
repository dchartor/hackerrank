def electronic shops(key, usb, b)
    a = []
    try:
        for i in key:
            for j in usb:
                if i + j <= b:
                    a.append(i + j)

        return max(a)
    except:
        return -1
