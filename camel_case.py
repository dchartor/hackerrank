def camel_case(s):
    return sum([1 for x in s if x.isupper()]) + 1


print(camel_case('saveChangesInTheEditor'))
