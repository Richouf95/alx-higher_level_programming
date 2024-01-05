#!/usr/bin/python3
"""
    Text indentation
"""
def text_indentation(text):
    """
        This function indente a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tokens = []
    start = 0

    for i, c in enumerate(text):
        if c in ".?:\n":  # Include "\n" as a delimiter
            if i + 1 <= len(text) - 1:
                tok = text[start:i+1].lstrip().rstrip()
                tokens.append(tok)
                start = i + 1

    tok = text[start:].lstrip()
    tokens.append(tok)
    for i, token in enumerate(tokens):
        tokenLenght = len(token)
        x = 0
        temp = ""
        last = ""
        while x <= tokenLenght - 1:
            if x == tokenLenght - 1:
                last = token[x]
            else:
                temp += token[x]
            x += 1
        t = temp.lstrip().rstrip()
        if last != " ":
            tokens[i] = t + last
        else:
            tokens[i] = t

    for t, token in enumerate(tokens):
        if token == "":
            tokens.remove(token)

    pos = 0
    tokenLenght = len(tokens) - 1
    for x in tokens:
        if pos == tokenLenght:
            if x and x[-1] in ".?:":
                print(x)
                print()
            else x:
                print(x, end=" ")
        else:
            print(x)
            print()
        pos += 1
