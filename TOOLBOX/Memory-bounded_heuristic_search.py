import tkinter as tk
from tkinter import messagebox

class GraphNode:
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []


def mbhs(node, target, memory_limit, visited=None):
    if node.value == target:
        return node

    if memory_usage(node) > memory_limit:
        return None

    if visited is None:
        visited = set()
    visited.add(node)

    for neighbor in node.neighbors:
        if neighbor not in visited:
            result = mbhs(neighbor, target, memory_limit, visited)
            if result is not None:
                return result

    return None


def memory_usage(node):
    import sys
    return sys.getsizeof(node)


class GraphVisualization(tk.Tk):
    def __init__(self, start_node, result_path):
        super().__init__()
        self.title("Graph Visualization")
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()

        self.node_positions = {}
        self.node_radius = 20
        self.calculate_node_positions(start_node, 0, 100, 200)
        self.draw_graph(start_node, result_path)

    def calculate_node_positions(self, node, level, x, y):
        self.node_positions[node] = (x, y)
        y_offset = 100

        for neighbor in node.neighbors:
            if neighbor not in self.node_positions:
                self.calculate_node_positions(neighbor, level + 1, x + (level + 1) * 50, y + y_offset)
                y_offset += 50

    def draw_graph(self, start_node, result_path):
        for node, position in self.node_positions.items():
            if node in result_path:
                color = "green"  # Color the nodes in the result path as green
            else:
                color = "lightblue"
            self.draw_node(position[0], position[1], node.value, color)

            for neighbor in node.neighbors:
                neighbor_position = self.node_positions[neighbor]
                self.draw_edge(position[0], position[1], neighbor_position[0], neighbor_position[1])

    def draw_node(self, x, y, value, color):
        self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill=color)
        self.canvas.create_text(x, y, text=value)

    def draw_edge(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)


def create_graph():
    print("Enter the number of nodes in the graph:")
    num_nodes = int(input())

    nodes = {}
    for i in range(num_nodes):
        print("Enter the value for node", i + 1)
        value = input()
        nodes[i] = GraphNode(value)

    print("Enter the number of edges in the graph:")
    num_edges = int(input())

    edges = []
    for _ in range(num_edges):
        print("Enter the nodes connected by an edge (space-separated values):")
        node_values = input().split()
        edges.append(node_values)

    for edge in edges:
        value1, value2 = edge
        node1 = next((node for node in nodes.values() if node.value == value1), None)
        node2 = next((node for node in nodes.values() if node.value == value2), None)
        if node1 and node2:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)

    print("Enter the index of the starting node:")
    start_index = int(input())
    start_node = nodes[start_index]

    return start_node


# Create the graph from user input
print("Create a graph:")
start_node = create_graph()

# Search for a value with a memory limit
target_value = input("Enter the value to search: ")
memory_limit = int(input("Enter the memory limit in bytes: "))

# Perform the search
result = mbhs(start_node, target_value, memory_limit)

if result is not None:
    result_path = [result]
    messagebox.showinfo("Search Result", "Node with value '{}' found!".format(target_value))
else:
    result_path = []
    messagebox.showinfo("Search Result", "Node with value '{}' not found or memory limit reached.".format(target_value))

# Visualize the graph with the result path
graph_gui = GraphVisualization(start_node, result_path)
graph_gui.mainloop()
