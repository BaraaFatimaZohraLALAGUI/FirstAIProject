#Greedy BFS

import heapq
import tkinter as tk
from graph2 import GraphVisualization 

# A heuristic function that calculates the Euclidean distance between two nodes
def heuristic(node, goal):
    return abs(ord(node) - ord(goal))

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def Greedy_BFS(self, start_node, goal_node):
        # Create a priority queue with initial node, its heuristic value, and an empty path
        queue = [(heuristic(start_node, goal_node), start_node, [])]

        # Set to keep track of visited nodes
        visited = set()

        # Convert the queue into a heap
        heapq.heapify(queue)

        # Continue until the queue is empty
        while queue:
            # Pop the node with the lowest heuristic value from the queue
            (h, node, path) = heapq.heappop(queue)

            # Check if the node has not been visited
            if node not in visited:
                # Mark the node as visited
                visited.add(node)

                # Extend the current path with the current node
                path = path + [node]

                # Check if the current node is the goal node
                if node == goal_node:
                    return path

                # Iterate over the neighbors of the current node
                for neighbor in self.adjacency_list[node]:
                    # Check if the neighbor has not been visited
                    if neighbor not in visited:
                        # Push the neighbor into the queue with its heuristic value and updated path
                        heapq.heappush(queue, (heuristic(neighbor, goal_node), neighbor, path))

        # If the goal node is not reachable, return None
        return None


# Function to handle the button click event
def visualize_graph(graph, start_node, goal_node,window):
    # Create the graph and find the path
    graph = Graph(graph)
    # Call the BFS algorithm with the start and stop nodes
    path = graph.Greedy_BFS(start_node, goal_node)

    # Create the graph visualization canvas
    graph_canvas = GraphVisualization(window, graph, path)
    graph_canvas.pack()

# example of adjacency list for the graph
adjacency_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}


#example of how to Define the coordinates for node positions
node_coordinates = {
    'A': (50, 50),
    'B': (100, 50),
    'C': (50, 100),
    'D': (100, 100),
    'E': (150, 50),
    'F': (150, 100),
    'G': (200, 100)
}

