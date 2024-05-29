import os
import random
import tkinter as tk
from tkinter import messagebox

class CupGame:
    def __init__(self, master):
        self.master = master
        master.title("Cup Game")
        master.geometry("800x600")

        # Create background canvas
        self.canvas = tk.Canvas(master, bg="green")
        self.canvas.pack(fill="both", expand=True)

        # Create labels and entry fields
        self.cups_label = tk.Label(master, text="Number of Cups:", font=("Arial", 16))
        self.cups_label.place(relx=0.5, rely=0.1, anchor="center")

        self.cups_entry = tk.Entry(master, font=("Arial", 16))
        self.cups_entry.place(relx=0.5, rely=0.15, anchor="center")
        self.cups_entry.insert(0, "1")

        self.guesses_label = tk.Label(master, text="Number of Guesses:", font=("Arial", 16))
        self.guesses_label.place(relx=0.5, rely=0.2, anchor="center")

        self.guesses_entry = tk.Entry(master, font=("Arial", 16))
        self.guesses_entry.place(relx=0.5, rely=0.25, anchor="center")

        self.start_button = tk.Button(master, text="Start Game", font=("Arial", 16), command=self.start_game, bg="yellow")
        self.start_button.place(relx=0.5, rely=0.3, anchor="center")

        # Load cup and flower images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, "assets")
        self.cup_image = tk.PhotoImage(file=os.path.join(assets_dir, "cup.png"))
        self.flower_image = tk.PhotoImage(file=os.path.join(assets_dir, "flower.png"))

        # Initialize variables
        self.num_cups = 0
        self.num_guesses = 0
        self.remaining_guesses = 0
        self.guess_count = 0

    def start_game(self):
        self.num_cups = int(self.cups_entry.get())
        self.num_guesses = int(self.guesses_entry.get())

        if self.num_guesses < 1:
            messagebox.showerror("Invalid Guess", "Number of guesses must be at least 1.")
            return

        self.cups = list(range(1, self.num_cups + 1))
        flower_index = random.randint(0, self.num_cups - 1)
        self.cups[flower_index] = 'gol'

        self.remaining_guesses = self.num_guesses

        # Draw cups on the canvas
        self.draw_cups()

        # Start the guessing loop
        self.guessing_loop()

    def guessing_loop(self):
        self.create_guess_window()
        self.guess_window.wait_window()  # Wait for the guess window to close

        while self.remaining_guesses > 0:
            self.create_guess_window()
            self.guess_window.wait_window()  # Wait for the guess window to close

            if self.remaining_guesses == 0:
                messagebox.showinfo("Game Over", "You ran out of guesses!")
                self.master.destroy()
                break

    def create_guess_window(self):
        self.guess_window = tk.Toplevel(self.master)
        self.guess_window.title("Make a Guess")
        self.guess_window.geometry("400x200")

        self.guess_label = tk.Label(self.guess_window, text=f"Enter your guess (Remaining guesses: {self.remaining_guesses}):", font=("Arial", 16))
        self.guess_label.pack(pady=10)
        self.guess_entry = tk.Entry(self.guess_window, font=("Arial", 16))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.guess_window, text="Guess", font=("Arial", 16), command=self.make_guess, bg="lightgreen")
        self.guess_button.pack(pady=10)

    def draw_cups(self):
        self.canvas.delete("cup")
        cup_width = self.cup_image.width()
        cup_height = self.cup_image.height()
        spacing = (self.canvas.winfo_width() - cup_width * self.num_cups) // (self.num_cups + 1)

        start_x = (self.canvas.winfo_width() - (cup_width * self.num_cups + spacing * (self.num_cups - 1))) // 2

        for i in range(self.num_cups):
            x = start_x + i * (cup_width + spacing)
            y = self.canvas.winfo_height() // 2
            self.canvas.create_image(x, y, image=self.cup_image, tags=f"cup{i+1}")

    def make_guess(self):
        guess_index = int(self.guess_entry.get())

        if guess_index == 0:
            messagebox.showerror("Invalid Guess", "You cannot guess 0!")
            return

        if guess_index < 1 or guess_index > self.num_cups:
            messagebox.showerror("Invalid Guess", "Invalid cup number!")
            return

        self.guess_count += 1
        self.remaining_guesses -= 1

        if self.cups[guess_index - 1] == 'gol':
            self.canvas.delete("cup")
            self.draw_cups()
            cup_width = self.cup_image.width()
            cup_height = self.cup_image.height()
            spacing = (self.canvas.winfo_width() - cup_width * self.num_cups) // (self.num_cups + 1)
            start_x = (self.canvas.winfo_width() - (cup_width * self.num_cups + spacing * (self.num_cups - 1))) // 2
            x = start_x + (guess_index - 1) * (cup_width + spacing)
            y = self.canvas.winfo_height() // 2
            self.canvas.create_image(x, y, image=self.flower_image, tags="flower")
            messagebox.showinfo("Congratulations!", "You won!")
            self.guess_window.destroy()
            self.master.destroy()
            return

        self.guess_window.destroy()


