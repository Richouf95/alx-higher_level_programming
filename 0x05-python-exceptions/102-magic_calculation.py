#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for x in range(1, 3):
        try:
            result += a ** b / i
            if i > a:
                raise Exception("Too far")
        except Exception as e:
            result = a + b
            break
    return result
