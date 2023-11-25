import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def visualize_graph_Simulated_Annealing():
    def hill_climbing_search(graph, heuristic, initial_state):
        current_state = initial_state

        while True:
            neighbors = graph[current_state]
            best_neighbor = None
            best_heuristic = float('inf')

            for neighbor in neighbors:
                if heuristic[neighbor] < best_heuristic:
                    best_neighbor = neighbor
                    best_heuristic = heuristic[neighbor]

            if best_heuristic >= heuristic[current_state]:
                # Local maximum
                return current_state

            current_state = best_neighbor

    def draw_graph():
        # Get the input values
        graph_input = graph_entry.get()
        heuristic_input = heuristic_entry.get()
        initial_state = initial_state_entry.get()

        # Convert graph_input and heuristic_input to dictionaries
        graph = eval(graph_input)
        heuristic = eval(heuristic_input)

        # Create a NetworkX graph object
        G = nx.Graph(graph)

        # Apply hill climbing search
        best_solution = hill_climbing_search(graph, heuristic, initial_state)

        # Set node colors
        node_colors = ['green' if node == best_solution else 'lightblue' for node in G.nodes()]

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

    # Create input labels and entry fields
    graph_label = tk.Label(graph_window, text='Graph (Dictionary):')
    graph_label.pack()

    graph_entry = tk.Entry(graph_window)
    graph_entry.pack()

    heuristic_label = tk.Label(graph_window, text='Heuristic (Dictionary):')
    heuristic_label.pack()

    heuristic_entry = tk.Entry(graph_window)
    heuristic_entry.pack()

    initial_state_label = tk.Label(graph_window, text='Initial State:')
    initial_state_label.pack()

    initial_state_entry = tk.Entry(graph_window)
    initial_state_entry.pack()

    # Create the run button
    run_button = tk.Button(graph_window, text='Run Hill Climbing', command=draw_graph)
    run_button.pack()

    # Run the tkinter event loop
    graph_window.mainloop()


