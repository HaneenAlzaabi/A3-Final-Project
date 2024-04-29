# Import the required Python libraries
import time
import matplotlib.pyplot as plt
import networkx as nx
import random

#define the Vertex class
class Vertex:
    # Attributes for the Vertex class
    def __init__(self, vertex_id, name):
        self.vertex_id = vertex_id
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

    def plot_graph(self):
        # Determine the positions of the nodes
        pos = nx.spring_layout(self.network, scale=50.0)
        # Define the size of the figure
        plt.figure(figsize=(70, 100))
        # Get the names of the nodes to be used as labels
        labels = {node: data['name'] for node, data in self.network.nodes(data=True)}
        # Draw the nodes and edges of the graph
        nx.draw(self.network, pos, with_labels=False, node_color='skyblue', node_size=500, font_size=10, arrowsize=20)
        # Get the labels of the edges
        edge_labels = nx.get_edge_attributes(self.network, 'label')
        # Draw the labels of the edges
        nx.draw_networkx_edge_labels(self.network, pos, edge_labels=edge_labels, font_color='red')
        # Draw the labels of the nodes
        nx.draw_networkx_labels(self.network, pos, labels, font_size=12, font_color='purple', font_weight='bold')
        # Save the figure as a PDF
        plt.savefig("road_network_graph.pdf", format="pdf")
        plt.show()  # Display the figure

def time_complexity():
    # Defines the range of vertices
    vertices = range(1, 19)
    # Defines the range of edges
    edges = range(1, 19)
    # # Creates a list to store execution times
    times = []
    # Iterate over pairs of vertices and edges
    for v, e in zip(vertices, edges):
        # Record the start time
        start = time.time()
        graph = Graph()

        # Add vertices
        for i in range(v):
            # Add vertices to the graph
            graph.add_vertex(i, f'Vertex {i}')  # Add vertices to the graph

        # Add edges
        for i in range(e):
            # Add edges to the graph
            graph.add_edge(i, (i+1)%v, f"E{i}", random.randint(50, 200))  # Add edges to the graph

        # Record the end time
        end = time.time()  # Record the end time
        # Calculate the execution time and append it to the list
        times.append(end - start)

    # Plotting the results
    # Plot the execution times over the number of vertices
    plt.plot(vertices, times, label='Time complexity')
    # Set the label for x-axis
    plt.xlabel('Number of vertices and edges (V + E)')
    # Set the label for the y-axis
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.title('Time Complexity of Graph Operations')
    plt.show()

# Calls the function
time_complexity()
