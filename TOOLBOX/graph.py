import tkinter as tk
class GraphVisualization(tk.Canvas):
    def __init__(self, master, graph, path):
        super().__init__(master, width=800, height=600, bg='white')
        self.graph = graph
        self.path = path
        self.levels = {}  # Dictionary to store the levels of each node
        self.draw_graph()

    def draw_graph(self):
        max_depth = max(len(neighbors) for neighbors in self.graph.adjacency_list.values())
        level_height = 150  # Height between each level

        for node in self.graph.adjacency_list.keys():
            x = ord(node) - ord('A')  # Map node to x-coordinate
            depth = len(self.graph.adjacency_list[node])  # Get depth of the node
            y = (max_depth - depth) * level_height + 50  # Calculate y-coordinate based on depth
            self.levels[node] = y

            self.create_oval(x * 50 + 50, y, x * 50 + 70, y + 20, fill='lightblue', outline='black')
            self.create_text(x * 50 + 60, y + 10, text=node, fill='black')

        for node, neighbors in self.graph.adjacency_list.items():
            for neighbor, _ in neighbors:
                self.draw_edge(node, neighbor)

        for i in range(len(self.path) - 1):
            self.highlight_edge(self.path[i], self.path[i+1])

    def draw_edge(self, start, end):
        x1 = (ord(start) - ord('A')) * 50 + 60
        y1 = self.levels[start] + 10  # Adjust y-coordinate to connect with node center
        x2 = (ord(end) - ord('A')) * 50 + 60
        y2 = self.levels[end] + 10
        self.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill='black', width=1)

    def highlight_edge(self, start, end):
        x1 = (ord(start) - ord('A')) * 50 + 60
        y1 = self.levels[start] + 10  # Adjust y-coordinate to connect with node center
        x2 = (ord(end) - ord('A')) * 50 + 60
        y2 = self.levels[end] + 10
        self.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill='red', width=2)
