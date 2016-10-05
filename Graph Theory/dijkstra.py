import sys
import collections


class UndirectedGraphAM:

    def __init__(self):
        self.vertices = {}

    def add_edge(self,u,v,weight=0):
        edge_exists = False

        if u not in self.vertices:
            self.vertices[u] = {}
        else:
            if v in self.vertices[u]:
                current_weight = self.vertices[u][v]
                edge_exists = True

        if edge_exists:
            if weight < current_weight:
                self.vertices[u][v] = weight
        else:
            self.vertices[u][v] = weight


        if v not in self.vertices:
            self.vertices[v] = {}
        else:
            if u in self.vertices[v]:
                current_weight = self.vertices[v][u]
        if edge_exists:
            if weight < current_weight:
                self.vertices[v][u] = weight
        else:
            self.vertices[v][u] = weight

    def neighbours(self, u):
        if u in self.vertices:
            for i in self.vertices[u]:
                yield i

    def get_vertices(self):
        for i in self.vertices:
            yield i

    def get_weight(self, u,v):
        if u in self.vertices:
            if v in self.vertices[u]:
                return self.vertices[u][v]

    def __repr__(self):
        rep = "Graph: { "
        for u in self.vertices:
            rep += str(u) + ":"
            for v in self.vertices[u]:
                rep +="(" +str(v)
                if self.vertices[u][v]:
                    rep+= ","+str(self.vertices[u][v])+") "
                else:
                    rep+="), "
        return rep + "}"


class MinHeap:

    def __init__(self):
        self.heap = [0]
        self.currentsize = 0
        self.node_position_map = {}

    def insert(self, node):
        self.heap.append(node)
        self.currentsize = self.currentsize + 1
        self.node_position_map[node.key] = self.currentsize
        self.percolate_up(self.currentsize)

    def percolate_up(self,current_position):
        while current_position // 2 > 0:
            if self.heap[current_position] < self.heap[current_position // 2]:
                self.swap(current_position,current_position // 2)
            current_position = current_position // 2

    def swap(self, child_position, parent_position):
        child_node = self.heap[child_position]
        parent_node = self.heap[parent_position]
        self.node_position_map[child_node.key] = parent_position
        self.node_position_map[parent_node.key] = child_position
        self.heap[parent_position], self.heap[child_position] = self.heap[child_position], self.heap[parent_position]

    def extract_min(self):
        minval = self.heap[1]
        del self.node_position_map[minval.key]
        self.heap[1] = self.heap[self.currentsize]
        self.node_position_map[self.heap[1].key] = 1
        self.heap.pop()
        self.currentsize = self.currentsize - 1
        self.percolate_down(1)
        return minval

    def percolate_down(self, position):
        while position*2 <= self.currentsize:
            min_child_position = self.get_min_child_position(position)
            if self.heap[position] > self.heap[min_child_position]:
                self.swap(position, min_child_position)
            position = min_child_position

    def get_min_child_position(self, position):
        if (position * 2 + 1) > self.currentsize:
            return position * 2
        else:
            if self.heap[position * 2] < self.heap[position * 2 + 1]:
                return position * 2
            else:
                return position * 2 + 1

    def decrease_key(self, key, value):
        if key in self.node_position_map:
            position = self.node_position_map[key]
            self.heap[position] = HeapNode(key, value)
            self.percolate_up(position)

    def is_empty(self):
        return True if self.currentsize == 0  else False

    def __getitem__(self, key):
        position = self.node_position_map[key]
        return self.heap[position]

    def __contains__(self, item):
        return True if item in self.node_position_map else False


class HeapNode:

    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __gt__(self, other):
        return True if self.value > other.value else False

    def __lt__(self, other):
        return True if self.value < other.value else False

    def __le__(self, other):
        return True if self.value <= other.value else False

    def __ge__(self, other):
        return True if self.value >= other.value else False

    def __repr__(self):
        return "("+str(self.key)+", "+str(self.value)+")"


def dijkstras_algorithm(graph, start_vertex):
    heap = MinHeap()
    vertex_distance_map = {}
    vertex_parent_path = {}

    for vertex in graph.get_vertices():
        heap.insert(HeapNode(vertex, sys.maxsize))
        vertex_distance_map[vertex] = sys.maxsize

    heap.decrease_key(start_vertex, 0)
    vertex_distance_map[start_vertex] = 0
    vertex_parent_path[start_vertex] = None

    while not heap.is_empty():
        current_vertex = heap.extract_min()
        for next_vertex in graph.neighbours(current_vertex.key):
            if next_vertex in heap:
                new_cost = vertex_distance_map[current_vertex.key] + graph.get_weight(current_vertex.key,next_vertex)
                current_cost = heap[next_vertex].value
                if new_cost < current_cost:
                    vertex_distance_map[next_vertex] = new_cost
                    vertex_parent_path[next_vertex] = current_vertex.key
                    heap.decrease_key(next_vertex, new_cost)

    return vertex_distance_map


if __name__=='__main__':

    #file_input = 'dijkstra2_input.txt'
    #with open(file_input,'r+') as fobj:
    num_of_testcases = int(input().strip())
    for i in range(num_of_testcases):
            graph = UndirectedGraphAM()
            vertex, edges = (int(i) for i in input().strip().split(" "))
            for i in range(edges):
                u, v, weight = (int(i) for i in input().strip().split(" "))
                graph.add_edge(u, v, weight)
            start_vertex = int(input().strip())
            result = dijkstras_algorithm(graph, start_vertex)
            od = collections.OrderedDict(sorted(result.items()))
            for i in range(1,vertex+1):
                if i != start_vertex:
                    if i in od and od[i] != sys.maxsize:
                        print(od[i], end = " ")
                    else:
                        print(-1, end = " ")
            print()

