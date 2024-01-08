#!/usr/bin/python3
def element_at(my_list, idx):
    if not my_list or idx < 0 or idx > len(my_list) or my_list is None or idx is None:
        return None
    return my_list[idx]
