import heapq
import sys

class Graph:
    
    def __init__(self, vertices={}):
        self.vertices = vertices
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    vertices = {
    # building 1.2
    '1.2elevator':{'1.2corner1':1, '1.3elevator':4},
    '1.2corner1': {'1.201':1, '1.212':1, '1.213':2, '1.2elevator':1},
    '1.201': {'1.202': 1, '1.2corner1':1},
    '1.202': {'1.2corner2':1, '1.201':1},
    '1.2corner2': {'1.203':2, '1.202':1},
    '1.203': {'1.2corner3':2, '1.2corner2':2},
    '1.2corner3': {'1.207':3, '1.203':2},
    '1.207': {'1.2corner4': 2, '1.2corner3':3},
    '1.2corner4': {'1.207':3, '1.213':2, '1.209':3},
    '1.209': {'1.2corner4':3, '1.2corner5':1},
    '1.2corner5': {'1.210': 2, '1.209':1},
    '1.210': {'1.2corner6':2, '1.2corner5':2},
    '1.2corner6':{'1.212': 3, '1.210':2},
    '1.212': {'1.2corner1':1, '1.2corner6':3},
    '1.213': {'1.2corner1':2, '1.2corner4':2},
    # building 1.3
    '1.3elevator' :{'1.3corner1':1, '1.2elevator':4},
    '1.3corner1': {'1.301':1, '1.312':1, '1.313':2, '1.3elevator':1},
    '1.301': {'1.302': 1, '1.3corner1':1},
    '1.302': {'1.3corner2':1, '1.301':1},
    '1.3corner2': {'1.303':2, '1.302':1},
    '1.303': {'1.3corner3':2, '1.3corner2':2},
    '1.3corner3': {'1.307':3, '1.303':2},
    '1.307': {'1.3corner4': 2, '1.3corner3':3},
    '1.3corner4': {'1.307':3, '1.313':2, '1.309':3},
    '1.309': {'1.3corner4':3, '1.3corner5':1},
    '1.3corner5': {'1.310': 2, '1.309':1},
    '1.310': {'1.3corner6':2, '1.3corner5':2},
    '1.3corner6':{'1.312': 3, '1.310':2},
    '1.312': {'1.3corner1':1, '1.3corner6':3},
    '1.313': {'1.3corner1':2, '1.3corner4':2},
    }
    g = Graph(vertices)
    print(g.shortest_path('1.2elevator', '1.2corner1'))