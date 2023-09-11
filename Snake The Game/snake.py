from tkinter import *
import tkinter as tk
import random
import sys
import os


#Alle Variablen 
GAME_WIDTH = 900
GAME_HEIGHT = 800
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00' # Green
FOOD_COLOR = '#FF0000' # Red
BACKGROUND_COLOR = '#434750' # Black




class Snake:
    
    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake' )
            self.squares.append(square)


class Food:
    
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

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

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=(SNAKE_COLOR))

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

       global score

       score += 1
       
       label.config(text="Score:{}". format(score))

       canvas.delete('food')
       food = Food()

    else: 
       del snake.coordinates[-1]

       canvas.delete(snake.squares[-1])

       del snake.squares[-1]


    if check_collisions(snake):
       game_over()

    else:
       root.after(SPEED, next_turn, snake, food)
 
def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
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

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
           return True
    
    return False

def restart_script():
    # Schließt das aktuelle Python-Skript und startet es neu
    python = sys.executable
    os.execl(python, python, *sys.argv)

def game_over():
    canvas.delete(ALL)
    label.pack_forget()
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='Game Over', fill='#FF0000')
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/1.5, font=('consolas', 40), text='Score:'+ str(score), fill='#2E2E2E')
    restart_button.pack()
    

# Geöffnetes Fenster
root = tk.Tk()
root.title = ("SNAKE-GAME")
root.resizable(False, False)

restart_button = tk.Button(root, font=('consolas', 30), text="Restart", command=restart_script)

score = 0
direction = 'down'

label = Label(root, text='Score:{}'.format(score), font=('consolas', 30) )
label.pack()

canvas = Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.bind('<Left>', lambda event: change_direction('left'))
root.bind('<Right>', lambda event: change_direction('right'))
root.bind('<Up>', lambda event: change_direction('up'))
root.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

root.mainloop()