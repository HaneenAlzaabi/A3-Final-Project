import matplotlib.pyplot as plt
import networkx as nx
import random

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

# The function test_shortest_path_between_houses takes a graph, a source house and a target house,
# and prints the shortest path from source house to target house.
def test_shortest_path_between_houses(graph, source_house, target_house):
    # Get the shortest path from source house to target house.
    path, length = dijkstra_shortest_path(graph, source_house, target_house)
    # If a path exists, print the path and its length.
    if path is not None:
        print(f"Shortest path from House #{source_house} to House #{target_house} is {path} with length {length} meters")
        # Plot the graph with the shortest path highlighted.
        graph.plot_graph(source_house, target_house, path)
    # If no path exists, print a message indicating so.
    else:
        print(f"No path found from House #{source_house} to House #{target_house}")
    # Return the path and its length.
    return path, length

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

#Add vertices to the graph, each representing a house.
for i in range(20):
    graph.add_vertex(i, names[i])

# Add edges to the graph, each representing a street.
# Randomly assign a length to each street.
for i in range(19):
    graph.add_edge(i, i+1, f"E{i}", random.randint(50, 200))

# Add more random edges to the graph to increase its complexity.
for _ in range(10):
    v1, v2 = random.sample(range(20), 2)
    graph.add_edge(v1, v2, f"E{v1}{v2}", random.randint(50, 200))

# Define the source house and the target house.
source_house = 0
target_house = 8

# Test the shortest path between the source house and the target house.
test_shortest_path_between_houses(graph, source_house, target_house)




