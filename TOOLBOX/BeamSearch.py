import tkinter as tk
from queue import PriorityQueue

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def beam_search(self, start_node, goal_node, beta):
        # Initialize priority queue to store paths
        pq = PriorityQueue()
        pq.put((0, [start_node]))

        while not pq.empty():
            _, current_path = pq.get()
            current_node = current_path[-1]

            if current_node == goal_node:
                return current_path

            neighbors = self.adjacency_list.get(current_node, [])
            for neighbor in neighbors:
                path_extended = current_path + [neighbor]
                pq.put((self.heuristic(neighbor, goal_node), path_extended))

            # Reduce the number of paths to the top beta paths
            if pq.qsize() > beta:
                for _ in range(pq.qsize() - beta):
                    pq.get()

        return []

    def heuristic(self, node, goal_node):
        # Replace this with your own heuristic function
        return 0


# Customized adjacency list for the graph
adjacency_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'D': ['H',"F"],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'C': []
}

# Create a Graph instance
graph = Graph(adjacency_list)

# Perform beam search
start_node = 'A'
goal_node = 'F'
beam_width = 3
best_path = graph.beam_search(start_node, goal_node, beam_width)

# Create a Tkinter window
window = tk.Tk()
window.title("Graph Visualization")

# Create a canvas to draw the graph
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Compute the coordinates for each node
node_coordinates = {}
x_start = 400  # X-coordinate for the root node
y_start = 50   # Y-coordinate for the root node
x_step = 100   # Horizontal spacing between nodes
y_step = 100   # Vertical spacing between levels

# Function to recursively compute the coordinates for each node
def compute_coordinates(node, x, y):
    node_coordinates[node] = (x, y)
    children = graph.adjacency_list[node]
    num_children = len(children)
    x_start_child = x - (num_children * x_step) // 2
    for child in children:
        compute_coordinates(child, x_start_child, y + y_step)
        x_start_child += x_step

# Compute the coordinates for all nodes
compute_coordinates(start_node, x_start, y_start)

# Draw the nodes and edges on the canvas
for node, coordinates in node_coordinates.items():
    x, y = coordinates
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
    canvas.create_text(x, y, text=node)

    for child in graph.adjacency_list[node]:
        x2, y2 = node_coordinates[child]
        canvas.create_line(x, y + 20, x2, y2 - 20)

# Highlight the best path
if best_path:
    for i in range(len(best_path) - 1):
        node1 = best_path[i]
        node2 = best_path[i+1]
        x1, y1 = node_coordinates[node1]
        x2, y2 = node_coordinates[node2]
        canvas.create_line(x1, y1 + 20, x2, y2 - 20, fill="red", width=3)
else:
    canvas.create_text(400, 300, text="No path found.")

# Start the Tkinter event loop
window.mainloop()
