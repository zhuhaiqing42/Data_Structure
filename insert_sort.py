# -*- coding: utf-8 -*-

def insert_sort(alist):
	n = len(alist)
	for i in range(1, n):
		for j in range(i, 0, -1):
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]
			else:
				break
	return alist



if __name__ == '__main__':
	
	list_sorted = insert_sort([49,38,65,97,76,13,27,49])
	print(list_sorted)

