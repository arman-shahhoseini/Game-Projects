import tkinter as tk
from tkinter import messagebox

class XOXOGame:
    def __init__(self, master):
        self.master = master
        self.master.title("XOXO Game")
        self.board = [' '] * 9
        self.current_player = 'X'
        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=' ', font=('Arial', 20), width=3, height=1, command=lambda i=i: self.play_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def play_move(self, index):
        if self.board[index] == ' ':
            self.buttons[index].config(text=self.current_player)
            self.board[index] = self.current_player
            if self.check_winner():
                self.show_result(f"Player {self.current_player} wins!")
            elif ' ' not in self.board:
                self.show_result("It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True
        return False

    def show_result(self, message):
        messagebox.showinfo("Game Result", message)
        self.reset_game()

    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

def main():
    root = tk.Tk()
    game = XOXOGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()




       

           

