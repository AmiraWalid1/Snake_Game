# Snake Game

This is a simple implementation of the classic Snake game in Python.

## Requirements

- Python 3
- curses library

## How to Run

To run the game, simply execute the `snake.py` script with Python 3:

```bash
python3 snake.py
```
## Game Rules
<ul>
    <li>The snake moves in the window and can change direction based on the arrow key pressed.</li>
    <li>The snake eats the food (represented by PI) to grow longer.</li>
    <li>The game ends if the snake hits the wall or its own body.</li>
</ul>

## Implementation Details
<ul>
    <li>The game uses the curses library to draw on the terminal window.</li>
    <li>The snake’s body is represented as a list of coordinates.</li>
    <li>The game loop checks for user input and the snake’s position to update the game state.</li>
</ul>

*Enjoy the game!*
