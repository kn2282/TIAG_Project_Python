import tkinter as tk
from .constants import *

class RandomProduction:
    def __init__(self, gui):
        self.gui = gui
        self.random_production_frame = tk.Frame(self.gui.root, bg = 'pink')
        self.entry = tk.Entry(self.random_production_frame)
        self.do_button = tk.Button(self.random_production_frame, text = 'DO', bg = 'grey')
        self.random_production_label = tk.Label(self.random_production_frame, text = 'Generate random', bg = 'yellow')

    def place(self):
        self.random_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + 3 * MAIN_GRAPH_OFFSET, relwidth = CHOOSE_RANDOM_WIDTH, relheight = CHOOSE_RANDOM_HEIGHT, anchor = 'ne')
        self.random_production_label.place(relwidth = 1, relheight = 0.4)
        self.entry.place(rely = 0.4, relwidth = 0.8, relheight = 0.6)
        self.do_button.place(relx = 0.8, rely = 0.4, relwidth = 0.2, relheight = 0.6)

