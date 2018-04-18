def ShellInsertSort(alist, dk):
	n = len(alist)
	for i in range(dk, n):
		if alist[i] < alist[i-dk]:
			tmp = alist[i]
			j = i-dk
			while j>=0:
				if tmp < alist[j]:
					alist[j+dk] = alist[j]
					alist[j] = tmp
				j -= dk
	return alist
 

def ShellSort(array, len_array):  # 希尔排序
	dk = int(len_array/2)  # 增量
	while(dk >= 1):
		ShellInsertSort(array, dk)
		print(">>:",array)
		dk = int(dk/2)



if __name__ == "__main__":
	array = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
	print(">:", array)
	ShellSort(array, len(array))
