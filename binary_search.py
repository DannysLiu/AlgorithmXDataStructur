#!/usr/bin/env python
def binary_search(l, num):
    lo_index = 0
    high_index = len(l) - 1
    while lo_index < high_index:
        mid = (lo_index + high_index) // 2
        if l[mid] < num:
            lo_index = mid + 1
        else:
            high_index = mid
    return lo_index


