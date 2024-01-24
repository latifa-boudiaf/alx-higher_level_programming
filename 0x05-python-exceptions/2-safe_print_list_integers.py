#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end='')
                c += 1
    except IndexError as e:
        print(f"IndexError: {e}")
    print()
    return c
