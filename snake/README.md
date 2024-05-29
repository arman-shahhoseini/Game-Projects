## Snake Game
This is a classic Snake game implementation using the Python turtle graphics library and the freegames module. The game allows the player to control a snake that grows longer as it eats food. The objective is to avoid colliding with the walls or the snake's own body.

## How to Run
Make sure you have Python installed on your system.
Install the freegames module by running the following command:
pip install freegames

Save the provided code in a file, e.g., snake.py.
''' Run the script: '''
    python snake.py

## Gameplay
''' Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.'''
The snake will move continuously in the chosen direction.
Eat the green food squares to grow the snake's length.
Avoid colliding with the walls or the snake's own body.
The game will display the current length of the snake in the console.
If the snake collides with a wall or itself, the game will end, and a red square will mark the collision point.
Code Overview
The code uses the turtle library for graphics and the freegames module for helper functions. Here's a brief overview of the main components:
food and snake are vectors representing the position of the food and the snake's body segments, respectively.
aim is a vector representing the current direction of the snake's movement.
change() function updates the aim vector based on the user's key input.
inside() function checks if the snake's head is within the game boundaries.
move() function handles the snake's movement, collision detection, and food consumption.
The setup() function initializes the game window and sets up event handlers for key input.
The move() function is called repeatedly using the ontimer() function to create the animation loop.

## 📞Created By :
 [![Linkedin Badge](https://img.shields.io/badge/-ArmanShahhoseini-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/arman-shahhoseini-4447152a0/)](https://www.linkedin.com/in/arman-shahhoseini-4447152a0)