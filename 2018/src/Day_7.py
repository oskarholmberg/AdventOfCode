import networkx as nx
import string
from collections import defaultdict

def get_graph(lines):
    G = nx.DiGraph()
    for line in lines:
        parts = line.split()
        G.add_edge(parts[1], parts[7])
    return G

def solve_p1(lines):
    print("Part 1:")
    print(''.join(nx.lexicographical_topological_sort(get_graph(lines))))
    print("\n")

def is_available(resource):
	return resource[1] >= (string.ascii_uppercase.index(str(resource[0]))+1)

def text(resource):
	if not resource: return "*"
	return resource[0]


def solve_p2(lines):
	graph = get_graph(lines)
	done = list()
	handled = list()
	queue = [node for node, in_degree in graph.in_degree() if in_degree == 0]
	second = 0
	workers = [i for i in range(2)]
	allocation = defaultdict(lambda: False)

	while(not set(done) == set(graph.nodes)):
		# Allocate available resources
		for worker in workers:
			if len(queue) > 0 and (not allocation[worker] or is_available(allocation[worker])):
				allocation[worker] = (queue.pop(0), 0)
		# Perform job
		for worker in workers:
			if(allocation[worker]):
				if is_available(allocation[worker]):
					done.append(allocation[worker][0])
					queue.extend([n for n in graph.successors(allocation[worker][0]) if n not in handled])
					handled.extend([n for n in graph.successors(allocation[worker][0]) if n not in handled])
				else:
					allocation[worker] = (allocation[worker][0], allocation[worker][1]+1)

		print(str(second) + "\t" + text(allocation[0]) + "\t" + text(allocation[1]) + "\t" + "".join(done))
		second += 1


	print("Part 2:")
	print(second)


lines = open("../inputs/Day_7.txt").read().split("\n")

solve_p1(lines)
solve_p2(lines)


