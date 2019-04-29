# Put your solution here.
import networkx as nx
import random

def solve(client):
    client.end()
    client.start()
    """
	self.graph = self.city = self.__read_graph__(graph_name)
    self.home = response['home']
    self.students = response['k'] 1~40
    self.bots = response['l']
    self.scout_time = response['s']

    self.v = len(self.graph) = 100
    self.e = self.graph.size() = 4950 = 99 + ... + 1

    self.time = 0
    self.cant_scout = [set() for _ in range(self.k + 1)]
    self.bot_count = [0] * (self.n + 1)

    G = client.graph
    G.nodes() [1, ..., 100]
    G.edges(data="weight") [(u, v, w)]
    G[97][98]["weight"] = w when u=97, v=98
    T = nx.minimum_spanning_tree(G)
    print(sorted(T.edges(data=True)))
    """
    all_students = list(range(1, client.students + 1)) 
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1)) 
    """
	# no scout
    G = client.graph
    dists = {}
    for u in range(1, client.v):
    	w = float("inf")
    	i = 0
    	for v in range(u+1, client.v+1):
    		temp = G[u][v]["weight"]
    		if temp < w:
    			w = temp
    			i = v
    	dists[(u, i)] = w

    now_loc = []
    bots = 0
    for u, v in dists.keys():
    	if bots < client.bots:
	    	if not u in now_loc:
	    		num = client.remote(u, v)
	    	if num == 1:
	    		bots += 1
	    		now_loc.append(v)

    for i in now_loc:
    	path = nx.shortest_path(G, i, client.home, weight="weight")
    	for i in range(len(path)-1):
        	client.remote(path[i], path[i+1])
    """   
	# scout all --> prob
    G = client.graph
    responses = []
    prob = {}
    for v in non_home:
    	response = client.scout(v, all_students)
    	responses.append(response)
    	prob[v] = 0
    	for i in response.values():
    		if i:
    			prob[v] += 1
    sorted_prob = sorted(prob.items(), key = lambda kv: -kv[1])

    bots = 0
    for v, w in sorted_prob:
    	path = nx.shortest_path(G, v, client.home, weight="weight")
    	if bots < client.bots:
	    	if client.remote(path[0], path[1]) == 1:
	    		bots += 1
	    		for i in range(1, len(path)-1):
	        		client.remote(path[i], path[i+1])

    client.end()
