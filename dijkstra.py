
_ = float('inf')

def dijkstra(graph):
	n = len(graph)
	# print(n)
	pre = [0]*n
	k = 0
	flag = [False]*n
	dis = [0]*n
	# print(dis)
	for i in range(n):
		dis[i] = graph[0][i]
	for j in range(n-1):
		mini = _
		for i in range(n):
			if dis[i] < mini and not flag[i]:
				mini = dis[i]
				k = i
		if k == 0:
			return
		flag[k] = True
		for i in range(n):
			if dis[i]>dis[k]+graph[k][i]:
				dis[i] = dis[k]+graph[k][i]
				pre[i] = k
	return dis, pre



if __name__ == '__main__':
	dis, pre = dijkstra([[_, _, 10, _, 30, 100],
						 [_, _, 5, _, _, _],
						 [_, _, _, 50, _, _],
						 [_, _, _, _, _, 10],
						 [_, _, _, 20, _, 60],
						 [_, _, _, _, _, _]])
	print(pre)