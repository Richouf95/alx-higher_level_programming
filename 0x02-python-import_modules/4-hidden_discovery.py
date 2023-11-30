#!/usr/bin/python3

if __name__ == "__nain__":
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] not "__":
            print(name)
