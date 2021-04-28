"""Implemention of the Maze ADT using a 2-D array."""
from arra import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def count(self):
        res = []
        start_row = self._start_cell.row
        start_col = self._start_cell.col
        cur_row = self._exit_cell.row
        cur_col = self._exit_cell.col
        while len(res) != 100:
            try:
                if self._maze_cells[cur_row - 1, cur_col] != self.MAZE_WALL:
                    res.append((cur_row - 1, cur_col))
                    cur_row = cur_row - 1
                    cur_col = cur_col
                elif self._maze_cells[cur_row, cur_col + 1] != self.MAZE_WALL:
                    res.append((cur_row, cur_col + 1))
                    cur_row = cur_row
                    cur_col = cur_col + 1
                elif self._maze_cells[cur_row + 1, cur_col] != self.MAZE_WALL:
                    res.append((cur_row + 1, cur_col))
                    cur_row = cur_row + 1
                    cur_col = cur_col
                elif self._maze_cells[cur_row, cur_col - 1] != self.MAZE_WALL:
                    res.append((cur_row, cur_col - 1))
                    cur_row = cur_row
                    cur_col = cur_col - 1
            except IndexError:
                continue
        count = 0
        for i in res:
            if i == (start_row, start_col):
                count += 1
        if count == 0:
            return False
        else:
            return True

        
                   
    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        count = 0
        lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        end_row = self._exit_cell.row
        end_col = self._exit_cell.col
        for i in lst:
            try:
                if self._maze_cells[end_row + i[0], end_col + i[1]] == None:
                    count += 1
            except IndexError:
                continue
        if count == 0:
            return False
        
        if self.count() == False:
            return False

        cur_row = self._start_cell.row
        cur_col = self._start_cell.col
        while self._exit_found(cur_row, cur_col) != True:
            try:
                if self._valid_move(cur_row - 1, cur_col) == True:
                    self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                    cur_row = cur_row - 1
                    cur_col = cur_col
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._valid_move(cur_row, cur_col + 1) == True:
                    self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                    cur_row = cur_row
                    cur_col = cur_col + 1
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._valid_move(cur_row + 1, cur_col) == True:
                    self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                    cur_row = cur_row + 1
                    cur_col = cur_col
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._valid_move(cur_row, cur_col - 1) == True:
                    self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                    cur_row = cur_row
                    cur_col = cur_col - 1
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._maze_cells[cur_row - 1, cur_col] == self.PATH_TOKEN:
                    self._maze_cells[cur_row, cur_col] = self.TRIED_TOKEN
                    cur_row = cur_row - 1
                    cur_col = cur_col
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._maze_cells[cur_row, cur_col + 1] == self.PATH_TOKEN:
                    self._maze_cells[cur_row, cur_col] = self.TRIED_TOKEN
                    cur_row = cur_row
                    cur_col = cur_col + 1
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._maze_cells[cur_row + 1, cur_col] == self.PATH_TOKEN:
                    self._maze_cells[cur_row, cur_col] = self.TRIED_TOKEN
                    cur_row = cur_row + 1
                    cur_col = cur_col
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
                elif self._maze_cells[cur_row, cur_col - 1] == self.PATH_TOKEN:
                    self._maze_cells[cur_row, cur_col] = self.TRIED_TOKEN
                    cur_row = cur_row
                    cur_col = cur_col - 1
                    if self._exit_found(cur_row, cur_col) == True:
                        self._maze_cells[cur_row, cur_col] = self.PATH_TOKEN
                        return True
            except IndexError:
                continue
 

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] != self.MAZE_WALL:
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        maze = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] == None:
                    maze += '_ '
                if self._maze_cells[row, col] == self.MAZE_WALL:
                    maze += '* '
                if self._maze_cells[row, col] == self.PATH_TOKEN:
                    maze += 'x '
                if self._maze_cells[row, col] == self.TRIED_TOKEN:
                    maze += 'o '
            maze += '\n'
        maze = maze[:-1]
        return maze


    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col

m = Maze(5, 5)
for i in range(0, 5):
    m.set_wall(0, i)
for i in range(1, 5):
    m.set_wall(i, 0)
for i in range(0, 2):
    m.set_wall(i, 4)
for i in range(2, 5):
    m.set_wall(4, i)
m.set_wall(3, 2)
m.set_wall(3, 3)
m.set_wall(1, 2)
m.set_start(4, 1)
m.set_wall(1, 3)
m.set_wall(2, 3)
m.set_exit(3, 4)
m.find_path()
print(str(m))
# m.reset()
# print(str(m))