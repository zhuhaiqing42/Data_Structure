# -*- coding: utf-8 -*-

def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    i, j = 0, 0
    result = []
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len_a and j < len_b:
        if b[j] < a[i]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
    if i == len_a:
        for k in b[j:]:
            result.append(k)
    else:
        for k in a[i:]:
            result.append(k)
    return result


def merge_sort(alist):
    len_alist = len(alist)
    if len_alist <= 1:
        return alist
    else:
        m = int(len_alist/2)
        left = merge_sort(alist[:m])
        right = merge_sort(alist[m:])
    return merge(left, right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))
