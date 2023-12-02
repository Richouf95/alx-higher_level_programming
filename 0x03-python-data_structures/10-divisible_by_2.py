#/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_result = my_list.copy()
    for i, v in enumerate(my_list):
        if v % 2 == 0:
            list_result[i] = True
        else:
            list_result[i] = False
    return list_result
