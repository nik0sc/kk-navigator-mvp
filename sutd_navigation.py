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
                path.append(start)
                path.reverse()
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

def generate_route(nodes):
    # assume we dont start from a corner here
    out_s = ""
    for i in range(len(nodes)):
        out_s += str(i) + ". "
        if "elevator" in nodes[i]:
            out_s += "reach " + nodes[i]
            current_floor = int(nodes[i][2])
            des_floor     = int(nodes[i+1][2])
            if current_floor > des_floor:
                out_s += ", and go down"
            else:
                out_s += ", and go up"
        elif "corner" in nodes[i]:
            out_s += "reach " + nodes[i]
            out_s += ", and turn left"
        else:
            out_s += "reach " + nodes[i]
        out_s += '\n'
        
    return out_s

if __name__ == '__main__':
    if True:
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
        '1.3elevator' :{'1.3corner1':1, '1.2elevator':4, '1.4elevator':4, '2.3elevator':4},
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
        # building 1.4
        '1.4elevator' :{'1.4corner1':1, '1.3elevator':4, '1.5elevator':4},
        '1.4corner1': {'1.401':1, '1.412':1, '1.413':2, '1.4elevator':1},
        '1.401': {'1.402': 1, '1.4corner1':1},
        '1.402': {'1.4corner2':1, '1.401':1},
        '1.4corner2': {'1.403':2, '1.402':1},
        '1.403': {'1.4corner3':2, '1.4corner2':2},
        '1.4corner3': {'1.407':3, '1.403':2},
        '1.407': {'1.4corner4': 2, '1.4corner3':3},
        '1.4corner4': {'1.407':3, '1.413':2, '1.409':3},
        '1.409': {'1.4corner4':3, '1.4corner5':1},
        '1.4corner5': {'1.410': 2, '1.409':1},
        '1.410': {'1.4corner6':2, '1.4corner5':2},
        '1.4corner6':{'1.412': 3, '1.410':2},
        '1.412': {'1.4corner1':1, '1.4corner6':3},
        '1.413': {'1.4corner1':2, '1.4corner4':2},
        # building 1.5
        '1.5elevator' :{'1.5corner1':1, '1.4elevator':4, '2.5elevator':4},
        '1.5corner1': {'1.501':1, '1.512':1, '1.513':2, '1.5elevator':1},
        '1.501': {'1.502': 1, '1.5corner1':1},
        '1.502': {'1.5corner2':1, '1.501':1},
        '1.5corner2': {'1.503':2, '1.502':1},
        '1.503': {'1.5corner3':2, '1.5corner2':2},
        '1.5corner3': {'1.507':3, '1.503':2},
        '1.507': {'1.5corner4': 2, '1.5corner3':3},
        '1.5corner4': {'1.507':3, '1.513':2, '1.509':3},
        '1.509': {'1.5corner4':3, '1.5corner5':1},
        '1.5corner5': {'1.510': 2, '1.509':1},
        '1.510': {'1.5corner6':2, '1.5corner5':2},
        '1.5corner6':{'1.512': 3, '1.510':2},
        '1.512': {'1.5corner1':1, '1.5corner6':3},
        '1.513': {'1.5corner1':2, '1.5corner4':2},

        # building 2.2
        '2.2elevator':{'2.2corner1':1, '2.3elevator':4},
        '2.2corner1': {'2.201':1, '2.212':1, '2.213':2, '2.2elevator':1},
        '2.201': {'2.202': 1, '2.2corner1':1},
        '2.202': {'2.2corner2':1, '2.201':1},
        '2.2corner2': {'2.203':2, '2.202':1},
        '2.203': {'2.2corner3':2, '2.2corner2':2},
        '2.2corner3': {'2.207':3, '2.203':2},
        '2.207': {'2.2corner4': 2, '2.2corner3':3},
        '2.2corner4': {'2.207':3, '2.213':2, '2.209':3},
        '2.209': {'2.2corner4':3, '2.2corner5':1},
        '2.2corner5': {'2.210': 2, '2.209':1},
        '2.210': {'2.2corner6':2, '2.2corner5':2},
        '2.2corner6':{'2.212': 3, '2.210':2},
        '2.212': {'2.2corner1':1, '2.2corner6':3},
        '2.213': {'2.2corner1':2, '2.2corner4':2},
        # building 2.3
        '2.3elevator' :{'2.3corner1':1, '2.2elevator':4, '2.4elevator':4, '1.3elevator':4},
        '2.3corner1': {'2.301':1, '2.312':1, '2.313':2, '2.3elevator':1},
        '2.301': {'2.302': 1, '2.3corner1':1},
        '2.302': {'2.3corner2':1, '2.301':1},
        '2.3corner2': {'2.303':2, '2.302':1},
        '2.303': {'2.3corner3':2, '2.3corner2':2},
        '2.3corner3': {'2.307':3, '2.303':2},
        '2.307': {'2.3corner4': 2, '2.3corner3':3},
        '2.3corner4': {'2.307':3, '2.313':2, '2.309':3},
        '2.309': {'2.3corner4':3, '2.3corner5':1},
        '2.3corner5': {'2.310': 2, '2.309':1},
        '2.310': {'2.3corner6':2, '2.3corner5':2},
        '2.3corner6':{'2.312': 3, '2.310':2},
        '2.312': {'2.3corner1':1, '2.3corner6':3},
        '2.313': {'2.3corner1':2, '2.3corner4':2},
        # building 2.4
        '2.4elevator' :{'2.4corner1':1, '2.3elevator':4, '2.5elevator':4},
        '2.4corner1': {'2.401':1, '2.412':1, '2.413':2, '2.4elevator':1},
        '2.401': {'2.402': 1, '2.4corner1':1},
        '2.402': {'2.4corner2':1, '2.401':1},
        '2.4corner2': {'2.403':2, '2.402':1},
        '2.403': {'2.4corner3':2, '2.4corner2':2},
        '2.4corner3': {'2.407':3, '2.403':2},
        '2.407': {'2.4corner4': 2, '2.4corner3':3},
        '2.4corner4': {'2.407':3, '2.413':2, '2.409':3},
        '2.409': {'2.4corner4':3, '2.4corner5':1},
        '2.4corner5': {'2.410': 2, '2.409':1},
        '2.410': {'2.4corner6':2, '2.4corner5':2},
        '2.4corner6':{'2.412': 3, '2.410':2},
        '2.412': {'2.4corner1':1, '2.4corner6':3},
        '2.413': {'2.4corner1':2, '2.4corner4':2},
        # building 2.5
        '2.5elevator' :{'2.5corner1':1, '2.4elevator':4, '1.5elevator':4},
        '2.5corner1': {'2.501':1, '2.512':1, '2.513':2, '2.5elevator':1},
        '2.501': {'2.502': 1, '2.5corner1':1},
        '2.502': {'2.5corner2':1, '2.501':1},
        '2.5corner2': {'2.503':2, '2.502':1},
        '2.503': {'2.5corner3':2, '2.5corner2':2},
        '2.5corner3': {'2.507':3, '2.503':2},
        '2.507': {'2.5corner4': 2, '2.5corner3':3},
        '2.5corner4': {'2.507':3, '2.513':2, '2.509':3},
        '2.509': {'2.5corner4':3, '2.5corner5':1},
        '2.5corner5': {'2.510': 2, '2.509':1},
        '2.510': {'2.5corner6':2, '2.5corner5':2},
        '2.5corner6':{'2.512': 3, '2.510':2},
        '2.512': {'2.5corner1':1, '2.5corner6':3},
        '2.513': {'2.5corner1':2, '2.5corner4':2},
        }
    g = Graph(vertices)
    nodes = g.shortest_path('1.2elevator', '1.5corner4')
    print(generate_route(nodes))