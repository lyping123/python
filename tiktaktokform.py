import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" "]*9

        self.buttons = []
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=('Arial', 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        self.status_label = tk.Label(master, text="Current Player: X", font=('Arial', 14))
        self.status_label.grid(row=3, columnspan=3)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state="disabled")
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Draw!", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True
        
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def reset_game(self):
        self.board = [" "]*9
        for button in self.buttons:
            button.config(text=" ", state="normal")
        self.current_player = "X"
        self.status_label.config(text="Current Player: X")


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
