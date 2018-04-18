#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: zhuhaiqing
'''
def Partition(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]
    # print(high, low)
    array[low] = key
    return low


def Qsort(array, low, high):
    if low < high:
        pivotloc = Partition(array, low, high)
        Qsort(array, low, pivotloc)
        Qsort(array, pivotloc+1, high)
    return array


if __name__ == '__main__':
    array = [49, 38, 65, 97, 76, 13, 27, 49]
    print(array)
    result = Qsort(array, 0, len(array)-1)
    print(result)






