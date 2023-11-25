import tkinter as tk
import os
import subprocess

# Function to start playing the game
def start_game():
    game_folder = "THE_GAME"
    game_file = "main.py"
    game_path = os.path.join(game_folder, game_file)
    subprocess.Popen(["python", game_path])

# Function to use the toolbox
def use_toolbox():
    toolbox_folder = "TOOLBOX"
    toolbox_file = "Main.py"
    toolbox_path = os.path.join(toolbox_folder, toolbox_file)
    subprocess.Popen(["python", toolbox_path])

# Create the main window
window = tk.Tk()
window.geometry("300x200") 

# Set the window title
window.title("Game and Toolbox Interface")

# Create the start game button
start_game_button = tk.Button(window, text="Start Game", command=start_game)
start_game_button.pack()

# Create the use toolbox button
use_toolbox_button = tk.Button(window, text="Use Toolbox", command=use_toolbox)
use_toolbox_button.pack()

# Start the GUI event loop
window.mainloop()