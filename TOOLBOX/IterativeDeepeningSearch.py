import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DepthLimitedSearch import dls_recursive

def visualize_graph_IDS():
    def iterative_deepening_search(graph, init_vertex, goal_vertex):
        depth_limit = 0

        while True:
            visited = set()
            path = []
            if dls_recursive(graph, init_vertex, visited, goal_vertex, path, depth_limit):
                return path
            depth_limit += 1

    def draw_graph():
        # Get the input values
        graph_input = graph_entry.get()
        init_vertex = init_vertex_entry.get()
        goal_vertex = goal_vertex_entry.get()

        # Convert graph_input to a dictionary
        graph = eval(graph_input)

        # Create a NetworkX graph object
        G = nx.Graph(graph)

        # Apply iterative deepening search
        result = iterative_deepening_search(graph, init_vertex, goal_vertex)

        # Set node colors
        node_colors = ['green' if node in result else 'lightblue' for node in G.nodes()]

        # Draw the graph using Matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
        plt.title('Graph Visualization')

        # Embed the Matplotlib figure in the tkinter window
        if hasattr(draw_graph, 'canvas'):
            draw_graph.canvas.get_tk_widget().pack_forget()
            plt.close(draw_graph.fig)

        draw_graph.fig = fig
        draw_graph.canvas = FigureCanvasTkAgg(fig, master=graph_window)
        draw_graph.canvas.draw()
        draw_graph.canvas.get_tk_widget().pack()

    # Create a tkinter window for graph visualization
    graph_window = tk.Tk()
    graph_window.title('Graph Visualization')
    graph_window.geometry('800x600')
    graph_window.protocol("WM_DELETE_WINDOW", graph_window.destroy)

    # Create input labels and entry fields
    graph_label = tk.Label(graph_window, text='Graph (Dictionary):')
    graph_label.pack()

    graph_entry = tk.Entry(graph_window, width = 50)
    graph_entry.pack()

    init_vertex_label = tk.Label(graph_window, text='Initial Vertex:')
    init_vertex_label.pack()

    init_vertex_entry = tk.Entry(graph_window, width = 50)
    init_vertex_entry.pack()

    goal_vertex_label = tk.Label(graph_window, text='Goal Vertex:')
    goal_vertex_label.pack()

    goal_vertex_entry = tk.Entry(graph_window, width = 50)
    goal_vertex_entry.pack()

    # Create the run button
    run_button = tk.Button(graph_window, text='Run Iterative Deepening Search', command=draw_graph)
    run_button.pack()

