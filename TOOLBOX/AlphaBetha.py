import tkinter as tk

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def utilityOfState(self, node):
        heuristic = 7
        return heuristic

    def minimax(self, node, alpha, beta, maximizing, depth):
        if depth == 0 or self.utilityOfState(node) != 0:
            return self.utilityOfState(node), node
        returnNode = node
        if maximizing:
            utility = float("-inf")
            for child in self.adjacency_list[node]:
                Nutility , Nnode = self.minimax(child, alpha, beta, False, depth - 1)
                if Nutility > utility:
                    utility = Nutility
                    returnNode = Nnode
                if utility > alpha:
                    alpha = utility
                if alpha >= beta:
                    break
            return utility, returnNode
        else:
            utility = float("inf")
            for child in self.adjacency_list[node]:
                Nutility, Nnode = self.minimax(child, alpha, beta, True, depth - 1)
                if Nutility < utility:
                    utility = Nutility
                    returnNode = Nnode
                if utility < beta:
                    beta = utility
                if alpha >= beta:
                    break
            return utility, returnNode

# Create an adjacency list representation of the graph
adjacency_list = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# Create a Graph instance
graph = Graph(adjacency_list)

# Create a Tkinter window
window = tk.Tk()
window.title("Graph Visualization")

# Create a canvas to draw the graph
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Compute the coordinates for each node based on levels
levels = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}
node_coordinates = {}
x_start = 400  # X-coordinate for the root node
y_start = 50   # Y-coordinate for the root node
x_step = 100   # Horizontal spacing between nodes
y_step = 100   # Vertical spacing between levels

# Function to recursively compute the coordinates for each node
def compute_coordinates(node, x, y):
    node_coordinates[node] = (x, y)
    children = graph.adjacency_list[node]
    num_children = len(children)
    x_start_child = x - (num_children * x_step) // 2
    for child in children:
        compute_coordinates(child, x_start_child, y + y_step)
        x_start_child += x_step

# Compute the coordinates for all nodes
compute_coordinates(1, x_start, y_start)

# Draw the nodes and edges on the canvas
for node, coordinates in node_coordinates.items():
    x, y = coordinates
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
    canvas.create_text(x, y, text=str(node))

    for child in graph.adjacency_list[node]:
        x2, y2 = node_coordinates[child]
        canvas.create_line(x, y + 20, x2, y2 - 20)

# Create a label to display the steps of the search
step_label = tk.Label(window, text="Steps:")
step_label.pack()

# Function to update the step label with the current search step
def update_step_label(step):
    step_label.config(text="Steps: " + step)

# Function to perform the minimax search with alpha-beta pruning and update the step label
def perform_search():
    search_steps = []

    def minimax_with_steps(node, alpha, beta, maximizing, depth):
        step = f"{node} (α={alpha}, β={beta})"  # Create a step string
        search_steps.append(step)
        update_step_label("\n".join(search_steps))

        if depth == 0:
            return graph.utilityOfState(node), node

        returnNode = node
        if maximizing:
            utility = float("-inf")
            for child in graph.adjacency_list[node]:
                Nutility, Nnode = minimax_with_steps(child, alpha, beta, False, depth - 1)
                if Nutility > utility:
                    utility = Nutility
                    returnNode = Nnode
                if utility > alpha:
                    alpha = utility
                if alpha >= beta:
                    break
                step = f"{node} (α={alpha}, β={beta})"  # Create a step string
                search_steps.append(step)
                update_step_label("\n".join(search_steps))
        else:
            utility = float("inf")
            for child in graph.adjacency_list[node]:
                Nutility, Nnode = minimax_with_steps(child, alpha, beta, True, depth - 1)
                if Nutility < utility:
                    utility = Nutility
                    returnNode = Nnode
                if utility < beta:
                    beta = utility
                if alpha >= beta:
                    break
                step = f"{node} (α={alpha}, β={beta})"  # Create a step string
                search_steps.append(step)
                update_step_label("\n".join(search_steps))

        return utility, returnNode

    minimax_with_steps(1, float("-inf"), float("inf"), True, 3)

# Button to start the search
search_button = tk.Button(window, text="Start Search", command=perform_search)
search_button.pack()

# Start the Tkinter event loop
window.mainloop()
