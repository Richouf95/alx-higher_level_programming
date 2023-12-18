#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
