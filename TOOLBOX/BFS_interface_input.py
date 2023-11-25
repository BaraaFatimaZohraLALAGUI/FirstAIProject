import tkinter as tk
import json
from BreadthFS import visualize_graph


def get_input_BFS():
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Breadth First Search Configuration")

    # Create a canvas for the window content
    canvas = tk.Canvas(window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a scrollbar for the canvas
    scrollbar = tk.Scrollbar(window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame to hold the window content
    content_frame = tk.Frame(canvas)

    # Add the content frame to the canvas
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Function to resize the canvas scrolling region
    def resize_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the resize_canvas function to the frame resize event
    content_frame.bind("<Configure>", resize_canvas)

    # Create a label for the instructions
    instructions_label = tk.Label(content_frame, text="Please fill in the required information:")
    instructions_label.pack(pady=10)

    # Create labels and entry fields for start node and goal node
    start_label = tk.Label(content_frame, text="Start Node:")
    start_label.pack()
    start_entry = tk.Entry(content_frame)
    start_entry.pack(pady=5)

    goal_label = tk.Label(content_frame, text="Goal Node:")
    goal_label.pack()
    goal_entry = tk.Entry(content_frame)
    goal_entry.pack(pady=5)

    # Create labels and text area for adjacency list
    adjacency_label = tk.Label(content_frame, text="Adjacency List:")
    adjacency_label.pack()
    adjacency_text_area = tk.Text(content_frame, height=10, width=40)
    adjacency_text_area.pack()

    def visualize_graph_wrapper():
        start_node = start_entry.get()
        goal_node = goal_entry.get()
        adjacency_list = adjacency_text_area.get("1.0", tk.END)

        try:
            adjacency_list = json.loads(adjacency_list)
        except json.JSONDecodeError as e:
            print("Invalid JSON input:", e)
            return

        # Call the visualize_graph function with the obtained input
        visualize_graph(adjacency_list, start_node, goal_node, window)

    visualize_button = tk.Button(content_frame, text="Visualize Graph", command=visualize_graph_wrapper)
    visualize_button.pack(pady=10)

    # Update the canvas scroll region after adding the content
    window.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


