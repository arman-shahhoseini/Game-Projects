import os
import tkinter as tk
from game import CupGame

os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = tk.Tk()
game = CupGame(root)
root.mainloop()
