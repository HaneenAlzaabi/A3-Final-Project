# Import required Python libraries
import matplotlib.pyplot as plt  # For creating plots
import networkx as nx  # For creating and managing graphs
import random  # For generating random numbers

# Defining the Graph class
class Graph:
    # Initialization function, which is called when a new object is created from the class
    def __init__(self):
        self.network = nx.DiGraph()  # Create an empty directed graph

    # Function to add a vertex (node) to the graph
    def add_vertex(self, vertex_id, name):
        self.network.add_node(vertex_id, name=name)  # Add a node with its id and name

    # Function to add an edge (connection between two nodes) to the graph
    def add_edge(self, from_vertex, to_vertex, edge_id, length):
        # Add an edge with its id, length and a label that is the length followed by 'm'
        self.network.add_edge(from_vertex, to_vertex, id=edge_id, length=length, label=f"{length}m")

    # Function to plot the graph
    def plot_graph(self):
        # Determine the positions of the nodes
        pos = nx.spring_layout(self.network, scale=50.0)
        # Define the size of the figure
        plt.figure(figsize=(70, 100))
        # Get the names of the nodes to be used as labels
        labels = {node: data['name'] if 'name' in data else str(node) for node, data in self.network.nodes(data=True)}
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

# Create the graph
graph = Graph()

# List of road names
names = ["Sheikh Zayed Road", "Corniche Road", "Al Salam Street", "Khalifa Street", "Airport Road",
         "Muroor Road", "Sheikh Rashid Bin Saeed Street", "Sultan Bin Zayed the First Street",
         "Sheikh Khalifa Bin Zayed Street", "Al Khaleej Al Arabi Street", "Al Falah Street",
         "Hamdan Street", "Electra Street", "Al Bateen Street", "Hazza Bin Zayed Street",
         "Saadiyat Island Highway", "Yas Island Highway", "Al Reem Island Highway",
         "Al Maryah Island Highway", "Sheikh Khalifa Bin Zayed Highway", "Al Maqtaa Bridge Road",
         "Al Ain Road", "Al Maktoum Street", "Al Raha Beach Road", "Mussafah Road",
         "Al Bahia Road", "Sheikh Mohammed Bin Zayed Road", "Al Wathba Road", "Al Karamah Street",
         "Al Jazira Al Arabiya Street", 'Al Quds Street', "Al Mina Road", "Al Ghurair Street", "Al Diyafah Street"]

# Shuffle the road names to get a random order
random.shuffle(names)

# Adding 10 vertices (nodes) to the graph
for i in range(10):
    graph.add_vertex(i, names[i])

# Add 9 edges (connections between nodes) to the graph
for i in range(9):
    # Make an edge from node i to node i+1 and have a random length between 50 and 200
    graph.add_edge(i, i+1, f"E{i}", random.randint(50, 200))

# Add 6 more edges to create intersections
for _ in range(6):
    # Select two different nodes randomly and add an edge between them
    v1, v2 = random.sample(range(10), 2)  # Sample 2 elements from the range of 10
    graph.add_edge(v1, v2, f"E{v1}{v2}", random.randint(50, 200))

# Plot the graph
graph.plot_graph()
