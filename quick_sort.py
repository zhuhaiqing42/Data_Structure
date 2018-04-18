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


# n = int(raw_input())
# tmp = []
# for i in range(n):
#     s = raw_input()
#     tmp.append(s)

# for i in range(n):
#     if len(tmp[i])<= 10:
#         print(tmp[i])
#     else:
#         s = tmp[i]
#         print(s[0]+str(len(s)-2)+s[-1])




  
# def prime(n):  
#     flag = [1]*(n+2)  
#     p=2 
#     prime_list = [] 
#     while(p<=n):  
#         prime_list.append(p)  
#         for i in xrange(2*p,n+1,p):  
#             flag[i] = 0  
#         while 1:  
#             p += 1  
#             if(flag[p]==1):  
#                 break
#     return prime_list 

# n = int(raw_input())
# prime_list = prime(n) 
# print(prime_list)

# tmp = []
# for i in range(int(len(prime_list)/2)):
#     for j in range(2, 10):
#         a = prime_list[i]**j
#         while a < n:
#             tmp.append(a)
# tmp.append(prime_list)
# print(tmp)



