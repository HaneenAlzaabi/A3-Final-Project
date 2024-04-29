# Import the required Python libraries
import matplotlib.pyplot as plt
import networkx as nx
import random
import time

#define the Vertex class
class Vertex:
    # Attributes for the Vertex class
    def __init__(self, vertex_id, name):
        self.vertex_id = vertex_id
        self.name = name

#Define the House class
class House:
    # Attributes for the House class
    def __init__(self, house_id, name):
        self.house_id = house_id
        self.name = name

#Define Edge class
class Edge:
    # Attributes for the Edge class
    def __init__(self, from_vertex, to_vertex, edge_id, length):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.edge_id = edge_id
        self.length = length

# Define Graph class
class Graph:
    def __init__(self):
        # Initialize the dictionary to store vertices
        self.vertices = {}
        # Initialize the dictionary to store houses
        self.houses = {}
        # Initialize a list to store edges
        self.edges = []
        # Creates a directed graph using networkx
        self.network = nx.DiGraph()

    def add_vertex(self, vertex_id, name):
        if vertex_id not in self.vertices:
            # Add a new vertex to the graph
            self.vertices[vertex_id] = Vertex(vertex_id, name)
            # Add the vertex to the networkx graph
            self.network.add_node(vertex_id, name=name)

#
    def add_house(self, house_id, name):
        # Check if the house ID is not already in the list of houses
        if house_id not in self.houses:
            # If the house ID is not in the list, create a new House object with the given ID and name
            self.houses[house_id] = House(house_id, name)
            # Add a node to the networkx graph with the house ID and name
            self.network.add_node(house_id, name=name)

    def add_edge(self, from_vertex, to_vertex, edge_id, length):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            # Create a new edge object
            edge = Edge(from_vertex, to_vertex, edge_id, length)
            # Add the edge to the list of edges
            self.edges.append(edge)
            # Add the edge to the networkx graph with attributes
            self.network.add_edge(from_vertex, to_vertex, id=edge_id, length=length, label=f"{length}m")

# This function measures the time complexity of finding the shortest path in a graph for the houses.
def measure_time_complexity(min_vertices, max_vertices, step):
    # This line creates a range of numbers from "min_vertices" to "max_vertices", increasing by "step" each time.
    vertices = range(min_vertices, max_vertices, step)
    # This is an empty list where we will store the time it takes to find the shortest path for each graph.
    times = []
    for vertex_count in vertices:
        graph = Graph()
        for i in range(vertex_count):
            graph.add_vertex(i, f'Vertex {i}')
        for i in range(vertex_count - 1):
            graph.add_edge(i, i+1, f"E{i}", random.randint(50, 1000))
        start_time = time.time()
        # We record the current time before we start finding the shortest path.
        nx.dijkstra_path(graph.network, source=0, target=vertex_count - 1, weight='length')
        end_time = time.time()
        # We calculate how long it took to find the shortest path and add it to the "times" list.
        times.append(end_time - start_time)

    return vertices, times

def plot_time_complexity(min_vertices, max_vertices, step):
    vertices, times = measure_time_complexity(min_vertices, max_vertices, step)
    plt.plot(vertices, times, label='Time complexity')
    plt.xlabel('Number of vertices')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.title('Time Complexity of Dijkstra Shortest Path Algorithm 2 ')
    plt.show()

# Call the function
plot_time_complexity(1, 25, 10)
