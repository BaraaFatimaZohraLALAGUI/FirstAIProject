import networkx as nx
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def depth_limited_search(graph, start, goal, depth_limit):
    visited = set()
    expanded_nodes = set()
    path = []

    dls_recursive(graph, start, visited, expanded_nodes, goal, path, depth_limit)

    if path:
        return path, expanded_nodes
    else:
        return None, expanded_nodes

def dls_recursive(graph, current_node, visited, expanded_nodes, goal_node, path, depth_limit):
    if current_node == goal_node:
        path.append(current_node)
        return True

    if depth_limit <= 0:
        return False

    visited.add(current_node)
    expanded_nodes.add(current_node)
    path.append(current_node)

    if current_node in graph:
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                if dls_recursive(graph, neighbor, visited, expanded_nodes, goal_node, path, depth_limit - 1):
                    return True

    path.pop()
    return False


def run_depth_limited_search():
    def visualize_graph():
        graph_input = graph_entry.get()
        start_node = start_entry.get()
        goal_node = goal_entry.get()
        depth_limit = int(depth_limit_entry.get())

        # Convert graph_input to a dictionary
        graph = eval(graph_input)

        path, expanded_nodes = depth_limited_search(graph, start_node, goal_node, depth_limit)
        
        if path is None:
            print("No path found within the depth limit.")
            expanded_nodes.update(visited_nodes)  # Add visited nodes to expanded nodes
        else:
            print("Path:", path)

        # Create a NetworkX graph object
        G = nx.Graph()

        # Add nodes and edges to the NetworkX graph object
        for node, neighbors in graph.items():
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        # Clear the previous graph from the canvas if it exists
        if hasattr(visualize_graph, 'canvas'):
            visualize_graph.canvas.get_tk_widget().pack_forget()
            plt.close(visualize_graph.fig)

        # Draw the graph using Matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(G)

        # Set node colors
        node_colors = []
        for node in G.nodes():
            if node in expanded_nodes:
                node_colors.append('red')  # Color the expanded nodes red
            elif path is not None and node in path:
                node_colors.append('green')  # Color the path nodes green
            else:
                node_colors.append('lightblue')  # Color other nodes light blue

        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
        plt.title('Graph Visualization')

        # Embed the Matplotlib figure in the tkinter window
        visualize_graph.fig = fig
        visualize_graph.canvas = FigureCanvasTkAgg(fig, master=window)
        visualize_graph.canvas.draw()
        visualize_graph.canvas.get_tk_widget().pack()

    # Create a tkinter window
    window = tk.Tk()
    window.title('Graph Visualization')
    window.geometry('800x600')

    # Create input labels and entry fields
    graph_label = tk.Label(window, text='Graph (Dictionary):')
    graph_label.pack()

    graph_entry = tk.Entry(window)
    graph_entry.pack()

    start_label = tk.Label(window, text='Start Node:')
    start_label.pack()

    start_entry = tk.Entry(window)
    start_entry.pack()

    goal_label = tk.Label(window, text='Goal Node:')
    goal_label.pack()

    goal_entry = tk.Entry(window)
    goal_entry.pack()

    depth_limit_label = tk.Label(window, text='Depth Limit:')
    depth_limit_label.pack()

    depth_limit_entry = tk.Entry(window)
    depth_limit_entry.pack()

    # Create the run button
    run_button = tk.Button(window, text='Run Depth-Limited Search', command=visualize_graph)
    run_button.pack()

    # Initialize visited nodes set
    visited_nodes = set()

    # Run the tkinter event loop
    window.mainloop()
