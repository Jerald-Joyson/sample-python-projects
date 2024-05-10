"""
🔴🔵 Connect Four: Rules & Regulations 🔵🔴

🔹 Objective: Connect Four is a classic two-player game where the goal is to be the first to form a line of four of your colored discs in a vertical, horizontal, or diagonal row on the game board.

🔹 Setup: The game board consists of a 6x7 grid. Players take turns dropping colored discs (red or blue) from the top into a column of their choice.

🔹 Gameplay: Players alternate turns, dropping one disc at a time into any of the seven columns. The disc falls to the lowest available space within the column.

🔹 Winning: The game is won by the first player to create a line of four of their own discs horizontally, vertically, or diagonally. If the game board fills up before either player achieves this, the game is a draw.

🔹 Strategic Thinking: Success in Connect Four requires both offensive and defensive strategies. Players must simultaneously aim to form their own lines of four while blocking their opponent from doing the same.

🔹 Etiquette: Sportsmanship and fair play are encouraged. Players should take turns respectfully and avoid disrupting the game flow. In case of disputes, a mutually agreed-upon resolution should be sought.

🔹 Enjoyment: Above all, Connect Four is a game of fun and friendly competition. So gather your friends or family, strategize, and enjoy the challenge of connecting four in a row!

Ready to challenge your friends to a game of Connect Four? Let the fun begin! 🎉
"""

# Program starts

import tkinter as tk
import tkinter.messagebox as msgbox
import random
import sys

class ConnectFourGUI:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Connect Four")

        # Constant values for the game interface
        self.GAME_BOARD_WIDTH = 500
        self.GAME_BOARD_HEIGHT = 500
        self.DISK_WIDTH = 70
        self.DISK_HEIGHT = 70
        self.PLAYER_1_COLOR = 'blue'
        self.PLAYER_2_COLOR = 'red'
        self.BACKGROUND_COLOR = 'grey'
        self.BORDER_COLOR = 'black'

        # Number of rows and columns on the game board
        self.rows = 6
        self.cols = 7

        # Dictionary to map player symbols to their colors
        self.colors = {'🔵': self.PLAYER_1_COLOR, '🔴': self.PLAYER_2_COLOR}

        # Initialize the game board with empty cells
        self.game_board = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        # Counter to keep track of turns
        self.turn_counter = 0

        # Initial current player
        self.current_player = '🔵'

        # Variable to store the winner
        self.winner = None

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create the canvas for drawing the game board
        self.canvas = tk.Canvas(self.root, width=self.GAME_BOARD_WIDTH, height=self.GAME_BOARD_HEIGHT, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

        # Calculate position to center the game board
        x0 = (self.GAME_BOARD_WIDTH - self.DISK_WIDTH * self.cols) // 2
        y0 = (self.GAME_BOARD_HEIGHT - self.DISK_HEIGHT * self.rows) // 2

        # Draw the game board grid
        self.draw_board(x0, y0)

        # Bind mouse click event to the drop_disc method
        self.canvas.bind("<Button-1>", self.drop_disc)

    def draw_board(self, x0, y0):
        # Draw the game board grid
        for row in range(self.rows):
            for col in range(self.cols):
                x = x0 + col * self.DISK_WIDTH
                y = y0 + row * self.DISK_HEIGHT
                self.canvas.create_rectangle(x, y, x + self.DISK_WIDTH, y + self.DISK_HEIGHT, outline=self.BORDER_COLOR, width=3)

    def drop_disc(self, event):
        # Method to handle dropping a disc into a column
        if not self.winner:
            # Calculate which column was clicked
            col = (event.x - (self.GAME_BOARD_WIDTH - self.DISK_WIDTH * self.cols) // 2) // self.DISK_WIDTH
            # Find the lowest empty row in the selected column
            for row in range(self.rows - 1, -1, -1):
                if self.game_board[row][col] == '':
                    # Place the disc in the lowest empty row
                    self.game_board[row][col] = self.current_player
                    # Draw the disc on the canvas
                    self.draw_disc(row, col)
                    # Check if the current player has won
                    if self.check_for_winner(row, col):
                        self.winner = self.current_player
                        msgbox.showinfo("Winner", f"{self.winner} wins!")
                        self.root.destroy()  # Exit the game after it's over
                        break
                    # Check for a draw
                    if self.turn_counter == self.rows * self.cols - 1:
                        msgbox.showinfo("Draw", "The game ends in a draw!")
                        self.root.destroy()  # Exit the game after it's over
                    # Update turn count and switch players
                    self.turn_counter += 1
                    self.current_player = '🔵' if self.turn_counter % 2 == 0 else '🔴'
                    break


    def draw_disc(self, row, col):
        # Method to draw a disc on the canvas
        x0 = (self.GAME_BOARD_WIDTH - self.DISK_WIDTH * self.cols) // 2
        y0 = (self.GAME_BOARD_HEIGHT - self.DISK_HEIGHT * self.rows) // 2
        x = x0 + col * self.DISK_WIDTH + self.DISK_WIDTH // 2
        y = y0 + row * self.DISK_HEIGHT + self.DISK_HEIGHT // 2
        color = self.colors[self.game_board[row][col]]
        self.canvas.create_oval(x - self.DISK_WIDTH // 2, y - self.DISK_HEIGHT // 2, 
                                x + self.DISK_WIDTH // 2, y + self.DISK_HEIGHT // 2, fill=color)

    def check_for_winner(self, row, col):
        # Method to check if there is a winner
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 4):
                r = row + dr * i
                c = col + dc * i
                if 0 <= r < self.rows and 0 <= c < self.cols and self.game_board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r = row - dr * i
                c = col - dc * i
                if 0 <= r < self.rows and 0 <= c < self.cols and self.game_board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

if __name__ == "__main__":
    # Initialize Tkinter root window and start the game
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()
