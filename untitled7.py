import turtle
import time

# Set up screen
wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Maze Solver")
wn.setup(1366, 768)

# Create maze turtle
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.shape("square")
maze_turtle.shapesize(1.8, 1.8)
maze_turtle.penup()
maze_turtle.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.speed(0)

# Maze structure (0 = wall, 1 = path)
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Draw the maze
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = -300 + (x * 40)
            screen_y = 300 - (y * 40)
            if maze[y][x] == 0:
                maze_turtle.goto(screen_x, screen_y)
                maze_turtle.color("green")
                maze_turtle.stamp()

# Move in a given direction
def move_in_direction(x, y, direction):
    if direction == 0:  # Right
        return x + 1, y
    elif direction == 1:  # Down
        return x, y + 1
    elif direction == 2:  # Left
        return x - 1, y
    elif direction == 3:  # Up
        return x, y - 1

# Check if the current position is at the boundary (exit)
def is_exit(x, y):
    return x == 0 or y == 0 or x == len(maze[0]) - 1 or y == len(maze) - 1

# Follow the wall and find the exit
def follow_wall(x, y, direction):
    while True:
        if is_exit(x, y):
            print(f"Exit found at: ({x}, {y})")
            wn.bye()
            return True
        
        # Try to turn left first
        left_dir = (direction - 1) % 4
        nx, ny = move_in_direction(x, y, left_dir)
        if maze[ny][nx] == 1:
            x, y = nx, ny
            direction = left_dir
        else:
            # If can't turn left, move forward if possible
            nx, ny = move_in_direction(x, y, direction)
            if maze[ny][nx] == 1:
                x, y = nx, ny
            else:
                # If can't move forward, turn right
                direction = (direction + 1) % 4

        player.goto(-300 + (x * 40), 300 - (y * 40))
        time.sleep(0.05)

# Initial setup
draw_maze(maze)
player.goto(-260, 260)  # Starting position (1, 1)

# Start following the wall
follow_wall(1, 1, 0)  # Start moving to the right

# Main loop
wn.mainloop()
