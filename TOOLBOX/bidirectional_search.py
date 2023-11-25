import networkx as nx
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def bidirectional_search(graph, initial_state, goal_state):
    forward_queue = [initial_state]
    backward_queue = [goal_state]
    forward_visited = set([initial_state])
    backward_visited = set([goal_state])
    expanded_nodes_forward = set()
    expanded_nodes_backward = set()

    while forward_queue and backward_queue:
        # Forward search
        current_forward = forward_queue.pop(0)
        neighbors_forward = graph[current_forward]

        for neighbor in neighbors_forward:
            if neighbor in backward_visited:
                return "Goal state reached!", expanded_nodes_forward, expanded_nodes_backward
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)
                expanded_nodes_forward.add(neighbor)

        # Backward search
        current_backward = backward_queue.pop(0)
        neighbors_backward = graph[current_backward]

        for neighbor in neighbors_backward:
            if neighbor in forward_visited:
                return "Goal state reached!", expanded_nodes_forward, expanded_nodes_backward
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)
                expanded_nodes_backward.add(neighbor)

    return "Goal state is unreachable.", expanded_nodes_forward, expanded_nodes_backward


def run_bidirectional_search():
    def visualize_graph():
        graph_input = graph_entry.get()
        initial_state = initial_state_entry.get()
        goal_state = goal_state_entry.get()

        # Convert graph_input to a dictionary
        graph = eval(graph_input)

        result, expanded_nodes_forward, expanded_nodes_backward = bidirectional_search(graph, initial_state, goal_state)
        print(result)
        print(expanded_nodes_backward)

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

        # Find the nodes that are in both expanded sets
        common_nodes = expanded_nodes_forward.union(expanded_nodes_backward)

        # Draw the graph using Matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(G)
        node_colors = ['green' if node == goal_state else 'red' if node in common_nodes else 'lightblue' for node in G.nodes()]
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

    initial_state_label = tk.Label(window, text='Initial State:')
    initial_state_label.pack()
    initial_state_entry = tk.Entry(window)
    initial_state_entry.pack()

    goal_state_label = tk.Label(window, text='Goal State:')
    goal_state_label.pack()
    goal_state_entry = tk.Entry(window)
    goal_state_entry.pack()

    # Create the run button
    run_button = tk.Button(window, text='Run Bidirectional Search', command=visualize_graph)
    run_button.pack()



