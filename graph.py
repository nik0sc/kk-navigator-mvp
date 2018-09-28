# graph object definition
# generate_route function

import heapq
import sys

class Graph:

    def __init__(self, vertices={}):
        self.vertices = vertices

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}  # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start:  # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            # Vertex in nodes with smallest distance in distances
            smallest = heapq.heappop(nodes)[1]
            if smallest == finish:  # If the closest node is our target we're done so print the path
                path = []
                # Traverse through nodes til we reach the root which is 0
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                path.reverse()
                return path
            # All remaining vertices are inaccessible from source
            if distances[smallest] == sys.maxsize:
                break

            # Look at all the nodes that this vertex is attached to
            for neighbor in self.vertices[smallest]:
                # Alternative path distance
                alt = distances[smallest] + self.vertices[smallest][neighbor]
                # If there is a new shortest path update our priority queue (relax)
                if alt < distances[neighbor]:
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
            des_floor = int(nodes[i+1][2])
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