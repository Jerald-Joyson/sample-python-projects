import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player1_name = ""
        self.player2_name = ""
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_initial_screen()

    def create_initial_screen(self):
        # Create initial screen with player name entry fields and start button
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=20)
        
        # Player 1 entry label and field
        self.player1_label = tk.Label(self.entry_frame, text="Player 1 (X):")
        self.player1_label.grid(row=0, column=0, padx=5, pady=5)
        self.player1_entry = tk.Entry(self.entry_frame)
        self.player1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Player 2 entry label and field
        self.player2_label = tk.Label(self.entry_frame, text="Player 2 (O):")
        self.player2_label.grid(row=1, column=0, padx=5, pady=5)
        self.player2_entry = tk.Entry(self.entry_frame)
        self.player2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Start game button
        self.start_button = tk.Button(self.entry_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Center the window on the screen
        self.center_window()

    def center_window(self):
        # Calculate the center position of the window
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        # Set the window geometry to center it on the screen
        self.root.geometry(f"+{x}+{y}")

    def start_game(self):
        # Retrieve player names from entry fields and start the game
        self.player1_name = self.player1_entry.get()
        self.player2_name = self.player2_entry.get()
        self.entry_frame.destroy()  # Remove the initial screen
        self.create_board()  # Create the game board

    def create_board(self):
        # Create the game board with buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.buttons_frame, text="", font=("Helvetica", 20), width=5, height=2,
                                                command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # Handle player moves
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(row, col):
                messagebox.showinfo("Tic Tac Toe", f"{self.get_current_player_name()} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.toggle_player()

    def check_win(self, row, col):
        # Check for a win condition
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True  # Row win
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True  # Column win
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True  # Diagonal win (top-left to bottom-right)
        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True  # Diagonal win (top-right to bottom-left)
        return False

    def check_draw(self):
        # Check for a draw condition
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def toggle_player(self):
        # Switch between players
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_game(self):
        # Reset the game state
        self.buttons_frame.destroy()  # Remove the game board
        self.__init__(root)  # Reinitialize the game

    def get_current_player_name(self):
        # Get the name of the current player
        if self.current_player == "X":
            return self.player1_name
        else:
            return self.player2_name

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
