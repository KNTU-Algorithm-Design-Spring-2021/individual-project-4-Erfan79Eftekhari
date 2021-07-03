from collections import defaultdict
class Graph:
	def __init__(self,graph,graph_length):
		self.graph = graph
		self.r = graph_length
	def find_edge_disjoint_path(self, start, end):
		parent = [-1]*(self.r)
		mf = 0 
		while self.BFS(start, end, parent) :
			pf = float("Inf")
			s = end
			while(s != start):
				pf = min (pf, self.graph[parent[s]][s])
				s = parent[s]
			mf += pf
			v = end
			while(v != start):
				u = parent[v]
				self.graph[u][v] -= pf
				self.graph[v][u] += pf
				v = parent[v]
		return mf
	def BFS(self,s, t, parent):
		v =[False]*(self.r)
		q=[]
		q.append(s)
		v[s] = True
		while q:
			u = q.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if v[ind] == False and val > 0 :
					q.append(ind)
					v[ind] = True
					parent[ind] = u
		print(parent)
		if v[t]:
			return True
		else:
			return False


if __name__ == "__main__":
	s = 0
	e = 7
	graph = [[0, 1, 1, 1, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0],
			[0, 0, 0, 1, 0, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 1, 0],
			[0, 0, 1, 0, 0, 0, 0, 1],
			[0, 1, 0, 0, 1, 0, 0, 1],
			[0, 0, 0, 0, 0, 1, 0, 1],
			[0, 0, 0, 0, 0, 0, 0, 0]]
	g = Graph(graph,len(graph))
	print("from %d to %d: "%(s, e))
	print ("maximum %d edge-disjoint paths" %
			(g.find_edge_disjoint_path(s, e)))
