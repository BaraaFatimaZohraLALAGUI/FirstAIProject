from collections import deque
import tkinter as tk
from graph2 import GraphVisualization

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def BFS(self, start_node, goal_node):
        queue = deque([(start_node, [start_node])])  # Initialize a queue with the start node and its path
        visited = set()  # Initialize a set for visited nodes

        while queue:
            vertex, path = queue.popleft()  # Dequeue the vertex and its path from the left of the queue

            if vertex == goal_node:
                return path  # If the goal node is reached, return the path

            if vertex not in visited:
                visited.add(vertex)  # Mark the vertex as visited

                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        # Append the neighbor and its path (current path + neighbor) to the queue
                        queue.append((neighbor, path + [neighbor]))

        return None  # If the goal node is not reachable, return None


# Function to handle the button click event
def visualize_graph(graph, start_node, goal_node,window):
    # Create the graph and find the path
    graph = Graph(graph)
    # Call the BFS algorithm with the start and stop nodes
    path = graph.BFS(start_node, goal_node)

    # Create the graph visualization canvas
    graph_canvas = GraphVisualization(window, graph, path)
    graph_canvas.pack()
#example of adjacency list 
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

