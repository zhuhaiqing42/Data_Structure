
INFI = float('inf') # INFI indicate the infinity

def floyed(graph):
	n = len(graph)
	p = [[[False for i in range(n)] for j in range(n)] for k in range(n)]
	result = [[0 for i in range(n)] for j in range(n)]
	for v in range(n):
		for w in range(n):
			result[v][w] = graph[v][w]
			for u in range(n):
				if (result[v][w]<INFI):
					p[v][w][v] = True  # true 表示u是从v到w当前求得最短路径上的顶点
					p[v][w][w] = True

	for u in range(n):
		for v in range(n):
			for w in range(n): 
				if (result[v][u]+result[u][w]<result[v][w]):
					result[v][w] = result[v][u]+result[u][w]
					for i in range(n):
						p[v][w][i] = p[v][u][i] or p[u][w][i]

	return result, p





if __name__ == '__main__':
	# graph = [ [0,  5,   INFI, 7],
	# 		  [INFI,  0,  4,  2],
	# 		  [3,  3, 0, 2],
	# 		  [INFI, INFI, 1, 0]]

	graph = [[0,4,11],[6,0,2],[3,INFI,0]]
	result, p = floyed(graph)
	print(result)
	print(p)