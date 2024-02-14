import random
import time
from turtle import Screen
from cell_manager import CellManager

GRID_SIZE = 32
TICK_DURATION = 0.1

# Calculate screen size plus a small border
screen_size = (GRID_SIZE * 20) + 20

screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.tracer(0)

cell_manager = CellManager(GRID_SIZE)

grid_size = GRID_SIZE
grid = [[random.choice([0, 1]) for y in range(grid_size)] for x in range(grid_size)]


def count_neighbors(grid, x, y):
    """Count the number of neighbouring cells with a value of 1"""
    neighbors = 0
    for x_diff in [-1, 0, 1]:
        if (x + x_diff) < 0 or (x + x_diff) > (grid_size - 1):
            continue
        for y_diff in [-1, 0, 1]:
            if (y + y_diff) < 0 or (y + y_diff) > (grid_size - 1):
                continue
            if x_diff == 0 and y_diff == 0:
                continue
            if grid[x + x_diff][y + y_diff]:
                neighbors += 1
    return neighbors


def dead_or_alive(grid, x, y):
    """Calculate if each cell will be dead or alive next iteration"""
    current_cell = grid[x][y]
    neighbors = count_neighbors(grid, x, y)
    if current_cell:
        if neighbors < 2:
            return 0
        elif 2 <= neighbors <= 3:
            return 1
        elif neighbors > 3:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


def iterate(grid):
    """Iterate the grid to the next configuration"""
    return [
        [dead_or_alive(grid, x, y) for y in range(grid_size)] for x in range(grid_size)
    ]


while True:
    grid = iterate(grid)
    cell_manager.update_cells(grid)
    screen.update()
    time.sleep(TICK_DURATION)
