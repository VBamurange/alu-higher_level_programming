#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    div_checker = []
    for i in range(list_len):
        if my_list[i] % 2 == 0:
            div_checker.append(True)
        else:
            div_checker.append(False)
    return div_checker
