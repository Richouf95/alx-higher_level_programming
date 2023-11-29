#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    copy = ""
    if n < 0 and n > len(str):
        copy = str
        return copy
    while i < len(str):
        x = i
        i += 1
        if x == n:
            continue
        copy += str[x]
    return copy
