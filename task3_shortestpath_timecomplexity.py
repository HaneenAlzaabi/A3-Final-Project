import matplotlib.pyplot as plt
import networkx as nx
import random
import time
import numpy as np

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

    def add_edge(self, from_vertex, to_vertex, edge_id, length):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            # Create a new edge object
            edge = Edge(from_vertex, to_vertex, edge_id, length)
            # Add the edge to the list of edges
            self.edges.append(edge)
            # Add the edge to the networkx graph with attributes
            self.network.add_edge(from_vertex, to_vertex, id=edge_id, length=length, label=f"{length}m")

    # Define a function to plot the graph with optional parameters for a source node, target node, and path.
    def plot_graph(self, source=None, target=None,path=None):
        # Sets the position of nodes using the spring layout algorithm
        pos = nx.spring_layout(self.network,scale=50.0)
        plt.figure(figsize=(70, 100))
        # Creates a dictionary of node names to be used as labels
        labels = {node: data['name'] for node, data in self.network.nodes(data=True)}
        node_colors = ['skyblue' if node not in [source, target] else 'green' for node in self.network.nodes()]
        # Draws nodes on the plot
        nx.draw(self.network, pos, with_labels=False, node_color=node_colors, node_size=500, font_size=10,arrowsize=20)
        # Sets the color of the edges, red for path, black for others.
        edge_colors = ['black' if edge not in path else 'red' for edge in self.network.edges()]
        # Draws the edges on the plot.
        nx.draw_networkx_edges(self.network, pos, edge_color=edge_colors)
        # If a path is provided,
        if path:
            path_edges = list(zip(path, path[1:]))  # Creates a list of edges in the path.
            nx.draw_networkx_edges(self.network, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_labels(self.network, pos, labels, font_size=12, font_color='purple', font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.network, 'label')
        # Draws the edge labels on the graph.
        nx.draw_networkx_edge_labels(self.network, pos, edge_labels=edge_labels)
        plt.savefig("road_network_graph.pdf", format="pdf")  # Saves the plot as a PDF file.
        plt.show()  # Displays the plot.


# The function dijkstra_shortest_path takes a graph, a source vertex and a target vertex,
# and returns the shortest path from source to target.
def dijkstra_shortest_path(graph, source, target):
    try:
        # Using networkx's dijkstra_path function to compute the shortest path.
        path = nx.dijkstra_path(graph.network, source=source, target=target, weight='length')
        # Using networkx's dijkstra_path_length function to get the length of the path.
        path_length = nx.dijkstra_path_length(graph.network, source=source, target=target, weight='length')
        # Return the path and its length.
        return path, path_length
    # If there is no path from source to target, return None and infinity.
    except nx.NetworkXNoPath:
        return None, float('inf')

# The function measure_time_complexity takes two nodes (source_node and target_node) and a maximum number of nodes (max_nodes).
# It measures the time complexity of the dijkstra_shortest_path function by running it on a range of graph sizes.
# It returns the number of nodes, the time taken for each graph size, and the time taken for a graph with 15 nodes.
def measure_time_complexity(source_node, target_node, max_nodes):
    # This # Create a list of numbers from 1 to max_nodes
    num_nodes = list(range(1, max_nodes + 1))
    ## create an empty list to store the execution times.
    times = []
    # Initialize a variable to store the execution time for a graph with 15 nodes.
    time_node_15 = None
    for n in num_nodes:
        for i in range(n):
            # Add a vertex to the graph.
            graph.add_vertex(i, f"Node{i}")
        for i in range(n-1):
            # Add an edge to the graph.
            graph.add_edge(i, i+1, f"E{i}", random.randint(50, 200))
        for _ in range(n//10):
            # Select two random numbers from 0 to n-1.
            v1, v2 = random.sample(range(n), 2)
            # Add an edge between the two selected vertices.
            graph.add_edge(v1, v2, f"E{v1}{v2}", random.randint(50, 200))
        # Record the current time.
        start_time = time.time()
        # Run the dijkstra_shortest_path function on the graph.
        dijkstra_shortest_path(graph, source_node, target_node)
        # Record the current time.
        end_time = time.time()
        # Calculate the execution time and add it to the list of times.
        times.append(end_time - start_time)
        # If the number of nodes is 15
        if n == 15:
            # Store the execution time for the graph with 15 nodes.
            time_node_15 = end_time - start_time  # Store the execution time for the graph with 15 nodes.
    return num_nodes, times, time_node_15


graph = Graph()  # Create a new Graph object.

def plot_time_complexity(num_nodes, times, time_node_15):
    plt.figure(figsize=(10, 6))
    plt.plot(num_nodes, times, marker='o')
    if time_node_15 is not None:
        plt.scatter(15, time_node_15, color='red', label=f'Node 15 time: {time_node_15:.2f}s')
    plt.title('Time Complexity of Dijkstra\'s Algorithm 3')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function with the specific nodes
num_nodes, times, time_node_15 = measure_time_complexity(0, 15, 50)
plot_time_complexity(num_nodes, times, time_node_15)


