#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for ele in set_1:
        if ele not in set_2:
            pass
        else:
            new.append(ele)
    return new
