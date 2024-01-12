#!/usr/bin/python3
import random
import curses

# intialize curses library to create screen
screen = curses.initscr()

# hide the mouse curses
curses.curs_set(0)

# getmax y, x of screen
screen_height, screen_width = screen.getmaxyx()

# create new window
window = curses.newwin(screen_height, screen_width, 0, 0)

# allow window to recieve input from keyboard
window.keypad(1)

# set the time delay for update the screen
window.timeout(150)

# set the y, x cordinate for the intial position of snake
snk_y = screen_height // 2
snk_x = screen_width // 2

# define the intial position of the snake body
snake = [
    [snk_y, snk_x]
]

# create the food in the middle of the window
food = [(screen_height // 2), (screen_width // 2) + 1]

# add the food by using PI char
window.addch(food[0], food[1], curses.ACS_PI)

# set the intial movement direction to right
key = curses.KEY_RIGHT

# Create main loop that loop forever until player loser or quite
while True:
    # get the next key that will be pressed by the user
    next_key = window.getch()

    # if user doesnot input any thing (key = key) else (key = next_key)
    key = key if next_key == -1 else next_key

    # check if snake collided with the wall or itself
    if (snake[0][0] in [0, screen_height]
            or snake[0][1] in [0, screen_width]
            or snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # set the new position of the snake head
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # insert the new head in the first position of the snake list
    snake.insert(0, new_head)

    # check if snake ate food
    if snake[0] == food:
        food = None  # remove food

        while food is None:
            # generate new food if snake ate it
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]

            '''
            set new food to food if new food is not in the snake body
            else generate new food
            '''
            food = new_food if new_food not in snake else None

        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
