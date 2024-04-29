# Import the required Python libraries
import matplotlib.pyplot as plt
import networkx as nx
import random
from networkx.algorithms import shortest_path

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

    def deliver_package(self, from_vertex, to_house):
        path = shortest_path(self.network, source=from_vertex, target=to_house, weight='length')
        path_names = [self.network.nodes[i]['name'] for i in path]
        print(f"Deliver package from {self.vertices[from_vertex].name} to {self.houses[to_house].name} via path {path_names}")

graph = Graph()

names = ["Sheikh Zayed Road", "Corniche Road", "Al Salam Street", "Khalifa Street", "Airport Road",
         "Muroor Road", "Sheikh Rashid Bin Saeed Street", "Sultan Bin Zayed the First Street",
         "Sheikh Khalifa Bin Zayed Street", "Al Khaleej Al Arabi Street", "Al Falah Street",
         "Hamdan Street", "Electra Street", "Al Bateen Street", "Hazza Bin Zayed Street",
         "Saadiyat Island Highway", "Yas Island Highway", "Al Reem Island Highway",
         "Al Maryah Island Highway", "Sheikh Khalifa Bin Zayed Highway", "Al Maqtaa Bridge Road",
         "Al Ain Road", "Al Maktoum Street", "Al Raha Beach Road", "Mussafah Road",
         "Al Bahia Road", "Sheikh Mohammed Bin Zayed Road", "Al Wathba Road", "Al Karamah Street",
         "Al Jazira Al Arabiya Street"]

random.shuffle(names)

# Add 10 vertices (nodes) to the graph
for i in range(10):
    graph.add_vertex(i, names[i])

# Add 9 edges (connections between nodes) to the graph
for i in range(9):
    # Make an edge from node i to node i+1 and have a random length between 50 and 200
    graph.add_edge(i, i+1, f"E{i}", random.randint(50, 200))

# Add more edges to create intersections
for _ in range(6):
    v1, v2 = random.sample(range(20), 2)
    graph.add_edge(v1, v2, f"E{v1}{v2}", random.randint(50, 200))

# Add houses to the graph
for i in range(1, 6):
    graph.add_house(i, f"House {i}")

# Deliver packages to the houses
for i in range(1, 6):
    graph.deliver_package(0, i)

graph.plot_graph()

