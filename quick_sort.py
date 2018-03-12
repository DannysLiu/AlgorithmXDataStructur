#!/usr/bin/env python


def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        tmp = l[0]
        smaller = [i for i in l[1:] if i <= tmp]
        greater = [i for i in l[1:] if i > tmp]
        return quick_sort(smaller) + [tmp] + quick_sort(greater)


print quick_sort([1,3,1,5,7,2,6,4])