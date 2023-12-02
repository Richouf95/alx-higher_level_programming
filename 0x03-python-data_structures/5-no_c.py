def no_c(my_string):
    newString = ""
    length = len(my_string)

    for x in my_string:
        if x == "c" or x == "C":
            continue
        newString += x

    return newString
