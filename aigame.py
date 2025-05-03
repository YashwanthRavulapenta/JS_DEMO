import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x550")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.game_mode = None
        self.players = {"X": "Player 1", "O": "Player 2"}
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 24, 'bold'), pady=20, fg='#333')
        self.title.pack()

        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.pack(pady=10)

        self.mode_label = tk.Label(self.mode_frame, text="Select Game Mode:", font=('Arial', 12))
        self.mode_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.one_v_one_button = tk.Button(self.mode_frame, text="1 vs 1", font=('Arial', 12), width=10,
                                          command=lambda: self.set_game_mode(1), bg="#e0e0e0", relief="raised")
        self.one_v_one_button.grid(row=1, column=0, padx=5, pady=5)

        self.vs_ai_button = tk.Button(self.mode_frame, text="vs AI", font=('Arial', 12), width=10,
                                      command=lambda: self.set_game_mode(2), bg="#e0e0e0", relief="raised")
        self.vs_ai_button.grid(row=1, column=1, padx=5, pady=5)

        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(pady=10)
        self.name_frame.pack_forget()

        self.name_label1 = tk.Label(self.name_frame, text="Player 1 (X):", font=('Arial', 12))
        self.name_label1.grid(row=0, column=0, padx=10)

        self.name_entry1 = tk.Entry(self.name_frame, font=('Arial', 12))
        self.name_entry1.grid(row=0, column=1)
        self.name_entry1.insert(0, "Player 1")

        self.name_label2 = tk.Label(self.name_frame, text="Player 2 (O):", font=('Arial', 12))
        self.name_label2.grid(row=1, column=0, padx=10)

        self.name_entry2 = tk.Entry(self.name_frame, font=('Arial', 12))
        self.name_entry2.grid(row=1, column=1)
        self.name_entry2.insert(0, "Player 2")

        self.start_button = tk.Button(self.root, text="Start Game", font=('Arial', 14), width=15,
                                      command=self.start_game, bg="#4CAF50", fg="white", relief="raised")
        self.start_button.pack(pady=10)
        self.start_button.pack_forget()

        self.turn_label = tk.Label(self.root, text="", font=('Arial', 14), fg='blue')
        self.turn_label.pack(pady=10)
        self.turn_label.pack_forget()

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = {}
        for i in range(9):
            button = tk.Button(self.board_frame, text=' ', font=('Arial', 24), width=5, height=2, relief="raised",
                               bg="#e0e0e0", command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons[i] = button
            self.buttons[i].config(state='disabled')

        self.reset_button = tk.Button(self.root, text="Reset Game", font=('Arial', 14), width=15,
                                      command=self.reset_game, bg="#f44336", fg="white", relief="raised")
        self.reset_button.pack(pady=10)
        self.reset_button.pack_forget()

    def set_game_mode(self, mode):
        self.game_mode = mode
        if mode == 1:
            self.players = {"X": "Player 1", "O": "Player 2"}
            self.name_entry1.delete(0, tk.END)
            self.name_entry1.insert(0, "Player 1")
            self.name_entry2.delete(0, tk.END)
            self.name_entry2.insert(0, "Player 2")
        elif mode == 2:
            self.players = {"X": "You", "O": "AI"}
            self.name_entry1.delete(0, tk.END)
            self.name_entry1.insert(0, "You")
            self.name_entry2.delete(0, tk.END)
            self.name_entry2.insert(0, "AI")

        self.mode_frame.pack_forget()
        self.name_frame.pack()
        self.start_button.pack()
        self.reset_button.pack()

    def start_game(self):
        if self.game_mode is None:
            messagebox.showwarning("Mode Selection", "Please select a game mode.")
            return

        player1_name = self.name_entry1.get()
        player2_name = self.name_entry2.get()

        if not player1_name or not player2_name:
            messagebox.showwarning("Name Error", "Please enter names for both players.")
            return

        self.players["X"] = player1_name
        self.players["O"] = player2_name
        self.start_button.config(state='disabled')
        self.name_entry1.config(state='disabled')
        self.name_entry2.config(state='disabled')
        self.turn_label.pack()
        self.update_turn_label()
        self.enable_grid_buttons()
        self.reset_button.pack()

        if self.game_mode == 2 and self.current_player == 'O':
            self.ai_move()

    def player_move(self, index):
        if self.board[index] == ' ' and not self.winner:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,
                                       fg="#4CAF50" if self.current_player == 'X' else "#F44336")
            winner = self.check_winner(self.board)
            if winner:
                self.winner = winner
                self.show_winner_message(self.players[winner])
            elif ' ' not in self.board:
                self.winner = 'Draw'
                self.show_draw_message()
            else:
                self.switch_player()
                if self.game_mode == 2 and self.current_player == 'O':
                    self.ai_move()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_turn_label()

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in win_combinations:
            if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
                return board[line[0]]
        return None

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        for i in range(9):
            self.buttons[i].config(text=' ', bg="#e0e0e0", fg="black", state='disabled')
        self.turn_label.config(text='')
        self.start_button.config(state='normal')
        self.name_entry1.config(state='normal')
        self.name_entry2.config(state='normal')
        self.mode_frame.pack()
        self.name_frame.pack_forget()
        self.start_button.pack_forget()
        self.turn_label.pack_forget()
        self.reset_button.pack_forget()

    def enable_grid_buttons(self):
        for button in self.buttons.values():
            button.config(state='normal')

    def update_turn_label(self):
        if self.game_mode == 1:
            self.turn_label.config(text=f"{self.players[self.current_player]}'s Turn ({self.current_player})")
        else:
            self.turn_label.config(text=f"{self.players[self.current_player]}'s Turn")
        self.turn_label.config(fg='blue' if self.current_player == 'X' else 'red')

    def show_winner_message(self, winner_name):
        messagebox.showinfo("Winner!", f"{winner_name} wins!")
        self.reset_game()

    def show_draw_message(self):
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset_game()

    def ai_move(self):
        if self.winner:
            return

        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        self.board[best_move] = 'O'
        self.buttons[best_move].config(text='O', fg="#F44336")

        winner = self.check_winner(self.board)
        if winner:
            self.winner = winner
            self.show_winner_message(self.players[winner])
        elif ' ' not in self.board:
            self.winner = 'Draw'
            self.show_draw_message()
        else:
            self.switch_player()

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

if __name__ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()