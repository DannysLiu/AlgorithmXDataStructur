#!/usr/bin/env python


def bubble_sort(l):
    length = len(l)
    for i in range(length):
        for j in range(length-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

