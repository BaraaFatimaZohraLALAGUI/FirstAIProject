#Uniform Cost Search

import tkinter as tk
import heapq
from graph import GraphVisualization

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def UCS(self, start_node, goal_node):
        visited = set()
        queue = [(0, start_node, [])]

        heapq.heapify(queue)

        while queue:
            cost, node, path = heapq.heappop(queue)

            if node not in visited:
                visited.add(node)
                path = path + [node]

                if node == goal_node:
                    return path

                for neighbor, neighbor_cost in self.adjacency_list[node]:  # Access the cost value from the adjacency list
                    if neighbor not in visited:
                        heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))

        return None

# Function to handle the button click event
def visualize_graph(graph, start_node, goal_node, window):
    # Create the graph and find the path
    graph = Graph(graph)
    # Call the UCS algorithm with the start and stop nodes
    path = graph.UCS(start_node, goal_node)

    # Create the graph visualization canvas
    graph_canvas = GraphVisualization(window, graph, path)
    graph_canvas.pack()

# example of adjacency list for the graph
adjacency_list = {
    'A': [('B', 2), ('C', 5), ('D', 1)],
    'B': [('E', 4)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [],
    'F': [],
    'G': []
}

