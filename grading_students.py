def gradingStudents(grades):
    from math import ceil
    l = []
    for i in grades:
        diff = abs(i - ceil(i / 5) * 5)
        if diff >= 3 or i < 38:
            l.append(i)
        else:
            l.append(diff + i)
    return l
