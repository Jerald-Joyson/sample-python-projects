from tkinter import *
from tkinter import messagebox
import random

# Constant values
GAME_WIDTH = 450
GAME_HEIGHT = 450
SPEED = 100
SPACE_SIZE = 15
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize snake's body coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Create rectangles representing snake's body parts
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    # Check if snake has eaten the food
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # Check for collisions
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    # Start the game loop only if direction is not empty
    if direction == '':
        direction = new_direction
        next_turn(snake, food)
        canvas.delete("initial_text")
    elif new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    # Check if snake has collided with walls or itself
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():

    # Delete all existing elements on canvas
    # canvas.delete(ALL)
    canvas.delete("gameover")
    canvas.delete("restart_button")
    canvas.delete("exit_button")
    canvas.delete("food")
    
    # Display game over text
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 - 20,
                       font=("Helvetica", 20), text="GAME OVER", fill="red", tag="gameover")

    # Create restart button
    restart_button = Button(window, text="Exit", command=exit_game )
    canvas.create_window(canvas.winfo_width()/2 + 40, canvas.winfo_height()/2 + 20, window=restart_button, tag=" exit_button")

    # Create exit button
    exit_button = Button(window, text="Restart", command=restart_game)
    canvas.create_window(canvas.winfo_width()/2 - 30, canvas.winfo_height()/2 + 20, window=exit_button,tag="restart_button")


def restart_game():
    global snake, food, score, direction


    for i in range(0, len(snake.squares)):
        canvas.delete(snake.squares[i])


    # Reset score and direction
    score = 0
    direction = ''

    # Update score label
    label.config(text="Score:{}".format(score))

    # Delete game over text and restart button
    canvas.delete("gameover")
    canvas.delete("restart_button")
    canvas.delete("exit_button")

    # Restart the game
    snake = Snake()
    food = Food()

def exit_game():
    window.destroy()

# Create Tkinter window
window = Tk()
window.title("Snake game")
window.resizable(False, False)

# Initialize variables
score = 0
direction = ''

# Create score label
label = Label(window, text="Score:{}".format(score), font=( 20))
label.pack()

# Create canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Position the window in the center of the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind arrow keys to change direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Create snake and food
snake = Snake()
food = Food()

canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 - 20,
    font=("Helvetica", 14), text="Click any arrow key to start the Game", fill="white", tag="initial_text")

# Run the Tkinter main loop
window.mainloop()
