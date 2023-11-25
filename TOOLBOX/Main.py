import tkinter as tk
import BFS_interface_input 
import UCS_interface_input 
import A_Search_input_interface 
import GBFS_input_interface 
import DepthFirstSearch 
import DepthLimitedSearch 
import bidirectional_search 
import hill_climbing 
import SimulatedAnnealingSearch 
import IterativeDeepeningSearch 

 
def create_strategy_button(strategy_name):
    # Create a button for the strategy with a command that calls the show_strategy_interface function
    button = tk.Button(buttons_frame, text=strategy_name, width=20, height=2, font=("Arial", 12),
                       command=lambda: show_strategy_interface(strategy_name))
    return button

def show_strategy_interface(strategy_name):
    # Create a new window for the strategy interface
    if strategy_name == "Breadth First Search":
        BFS_interface_input.get_input_BFS()
    elif strategy_name == "Uninformed Cost Search":
        UCS_interface_input.get_input_UCS()
    elif strategy_name == "Greedy Best First Search":
        GBFS_input_interface.get_input_GBFS()
    elif strategy_name == "A* Search":
        A_Search_input_interface.get_input_AS()
    elif strategy_name == "Depth First Search":
        DepthFirstSearch.run_depth_first_search()
    elif strategy_name == "Depth Limited Search":
        DepthLimitedSearch.run_depth_limited_search()
    elif strategy_name == "Bidirectional Search":
        bidirectional_search.run_bidirectional_search()
    elif strategy_name == "Hill Climbing":
        hill_climbing.visualize_graph_Hill_Climbing()   
    elif strategy_name == "Simulated Annealing": 
        SimulatedAnnealingSearch.visualize_graph_Simulated_Annealing()
    elif strategy_name == "Iterative Deepening Search":
        IterativeDeepeningSearch.visualize_graph_IDS()
    
    

# Create the main window
window = tk.Tk()
window.title("Problem Solving Toolbox")
window.geometry("800x500")

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to Problem Solving Toolbox!", font=("Arial", 18))
welcome_label.pack(pady=20)

# Create a label for the search strategy selection message
strategy_label = tk.Label(window, text="Please choose a strategy:", font=("Arial", 14))
strategy_label.pack(pady=10)

# Define the strategy names
strategies = [
    "Breadth First Search",
    "Depth First Search",
    "Depth Limited Search",
    "Uninformed Cost Search",
    "Iterative Deepening Search",
    "Bidirectional Search",
    "Greedy Best First Search",
    "A* Search",
    "Simulated Annealing",
    "Hill Climbing",
    "Memory-bounded heuristic search"
]
# Create a frame for the buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

# Create three columns for the buttons
columns = 3

# Calculate the number of rows needed based on the number of strategies and columns
rows = -(-len(strategies) // columns)  # Round up division

# Create buttons for each strategy
for i, strategy in enumerate(strategies):
    row = i // columns
    column = i % columns
    button = create_strategy_button(strategy)
    button.grid(row=row, column=column, padx=10, pady=10)

# Start the main event loop
window.mainloop()
