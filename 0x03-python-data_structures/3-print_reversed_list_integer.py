def print_reversed_list_integer(my_list=[]):
    reverseList = my_list
    reverseList.reverse()
    for x in reverseList:
        print("{}".format(x), end="\n")
