from turtle import Turtle

CELL_SIZE = 20


class CellManager:
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.cells = []
        self.create_cells(grid_size)

    def get_starting_coordinates(self, value):
        """Generates the coordinates for each cell."""
        start_x = -(self.grid_size * CELL_SIZE) / 2 + CELL_SIZE / 2
        start_y = (self.grid_size * CELL_SIZE) / 2 - CELL_SIZE / 2
        row = (value - 1) // self.grid_size
        col = (value - 1) % self.grid_size
        x = start_x + col * CELL_SIZE
        y = start_y - row * CELL_SIZE
        return (x, y)

    def create_cells(self, grid_size):
        """Creates all the turtles for the cells and positions them on the screen in a grid. Stored in a flat list for easy looping, not 2d"""
        for i in range(1, grid_size**2 + 1):
            cell_position = self.get_starting_coordinates(i)
            new_cell = Turtle()
            new_cell.shape("square")
            new_cell.color("white")
            new_cell.penup()
            new_cell.setpos(cell_position)
            self.cells.append(new_cell)

    def update_cells(self, number_list):
        """Updates the colors of the cells if alive or dead. Newly alive cells are blue for one tick, then remain black until dead."""
        flattened_list = self.flatten_2d_list(number_list)
        for i, alive in enumerate(flattened_list):
            if alive:
                if self.cells[i].color()[0] == "white":
                    self.cells[i].color("dark blue")
                else:
                    self.cells[i].color("black")
            else:
                self.cells[i].color("white")

    @staticmethod
    def flatten_2d_list(nested_list):
        """Used to flatten the input 2d list of 1's and 0's"""
        return [item for sublist in nested_list for item in sublist]
