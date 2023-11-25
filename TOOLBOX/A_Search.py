import tkinter as tk
from graph import GraphVisualization

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node, heuristic):
        open_list = set([start_node])
        closed_list = set([])

        g = {}
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# Function to handle the button click event
def visualize_graph(adjacency_list,start_node,goal_node,heuristic_function,window):

    # Create the graph and find the path
    graph = Graph(adjacency_list)

    # Call the A* algorithm with the start and stop nodes, and the heuristic function
    path = graph.a_star_algorithm(start_node, goal_node, heuristic_function)

    # Create the graph visualization canvas
    graph_canvas = GraphVisualization(window, graph, path)
    graph_canvas.pack()


# example of heuristic function
def my_heuristic(node):
    H = {
        'A': 1,
        'B': 3,
        'C': 2,
        'E': 0,
    }
    return H[node]


