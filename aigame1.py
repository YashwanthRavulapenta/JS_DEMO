import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.board = [' ' for _ in range(9)]  # Game board
        self.current_player = 'X'
        self.winner = None

        # Player names (set defaults initially)
        self.players = {"X": "Player 1", "O": "Player 2"}

        self.create_widgets()

    def create_widgets(self):
        """Create and display the main interface."""
        
        # Title
        self.title = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 24, 'bold'), pady=20, fg='#333')
        self.title.pack()

        # Player name inputs
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(pady=10)

        self.name_label1 = tk.Label(self.name_frame, text="Player 1 (X):", font=('Arial', 12))
        self.name_label1.grid(row=0, column=0, padx=10)

        self.name_entry1 = tk.Entry(self.name_frame, font=('Arial', 12))
        self.name_entry1.grid(row=0, column=1)

        self.name_label2 = tk.Label(self.name_frame, text="Player 2 (O):", font=('Arial', 12))
        self.name_label2.grid(row=1, column=0, padx=10)

        self.name_entry2 = tk.Entry(self.name_frame, font=('Arial', 12))
        self.name_entry2.grid(row=1, column=1)

        # Start button
        self.start_button = tk.Button(self.root, text="Start Game", font=('Arial', 14), width=15, command=self.set_player_names, bg="#4CAF50", fg="white", relief="raised")
        self.start_button.pack(pady=10)

        # Turn indicator
        self.turn_label = tk.Label(self.root, text="Player 1's Turn (X)", font=('Arial', 14), fg='blue')
        self.turn_label.pack(pady=10)

        # Game board (with colored buttons)
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = {}
        for i in range(9):
            button = tk.Button(self.board_frame, text=' ', font=('Arial', 24), width=5, height=2, relief="raised", bg="#e0e0e0",
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons[i] = button
            self.buttons[i].config(state='disabled')  # Disable all grid boxes initially

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", font=('Arial', 14), width=15, command=self.reset_game, bg="#f44336", fg="white", relief="raised")
        self.reset_button.pack(pady=10)

    def set_player_names(self):
        """Set player names and start the game."""
        player1_name = self.name_entry1.get()
        player2_name = self.name_entry2.get()

        if player1_name and player2_name:
            self.players["X"] = player1_name
            self.players["O"] = player2_name
            self.start_button.config(state='disabled')  # Disable the start button after game begins
            self.name_entry1.config(state='disabled')  # Disable name entry fields
            self.name_entry2.config(state='disabled')
            self.update_turn_label()
            self.enable_grid_buttons()  # Enable grid buttons after starting the game
        else:
            messagebox.showwarning("Name Error", "Please enter both player names.")

    def player_move(self, index):
        """Handle player's move when button is clicked."""
        if self.board[index] == ' ' and not self.winner:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="#4CAF50" if self.current_player == 'X' else "#F44336")
            if self.check_winner():
                self.winner = self.current_player
                winner_name = self.players[self.current_player]
                messagebox.showinfo("Winner!", f"{winner_name} wins!")
                self.display_winner(winner_name)
                self.reset_game()
            elif ' ' not in self.board:
                self.winner = 'Draw'
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def update_turn_label(self):
        """Update the turn label with the current player's name."""
        self.turn_label.config(text=f"{self.players[self.current_player]}'s Turn ({self.current_player})")
        self.turn_label.config(fg='blue' if self.current_player == 'X' else 'red')

    def switch_player(self):
        """Switch to the next player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_turn_label()

    def check_winner(self):
        """Check if there's a winner."""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for line in win_combinations:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return True
        return False

    def reset_game(self):
        """Reset the game state."""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        for i in range(9):
            self.buttons[i].config(text=' ', bg="#e0e0e0", fg="black")
        self.update_turn_label()
        self.start_button.config(state='normal')  # Enable start button again
        self.name_entry1.config(state='normal')  # Enable name entry fields
        self.name_entry2.config(state='normal')
        self.disable_grid_buttons()  # Disable the grid buttons after game reset

    def enable_grid_buttons(self):
        """Enable the grid buttons to allow player moves."""
        for button in self.buttons.values():
            button.config(state='normal')

    def disable_grid_buttons(self):
        """Disable the grid buttons to prevent player interaction."""
        for button in self.buttons.values():
            button.config(state='disabled')

    def display_winner(self, winner_name):
        """Display the winner's name in the center of the window."""
        self.winner_label = tk.Label(self.root, text=f"Winner: {winner_name}", font=('Arial', 20, 'bold'), fg='green')
        self.winner_label.pack(pady=20)
        self.root.after(2000, self.winner_label.destroy)  # Remove the winner label after 2 seconds

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
