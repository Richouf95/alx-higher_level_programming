#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    args = sys.argv
    if len(args) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if args[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    print("{} {} {} = {}".format(a, args[2], b, operators[args[2]](a, b)))
