from location import Location
from stack import Stack

class Maze():
    BREAD = 'B'
    EXIT = 'X'
    WALL = '#'
    PATH = ' '

    def __init__(self, fileName):
        file = open(fileName, "r")
        self.maze = self.make_maze(fileName)
        self.current = Location(1,0)
        self.paths = Stack()
        self.moves = [self.current]
        self.oops_index = 0

    def make_maze(self, fileName):
        file = open(fileName, "r")
        str_list = file.read().split('\n')
        maze = []

        for item in str_list:
            maze.append(list(item))

        return maze

    def solve_it(self):
        self.dropBC()
        self.current.moveRight()
        wandering = self.getMazeLocMark(self.current) != Maze.EXIT

        while wandering:
            self.dropBC()
            nextStep = self.pickDirection()
            self.moves.append(nextStep)
            self.takeAStep(nextStep)
            wandering = self.getMazeLocMark(self.current) != Maze.EXIT

        return self.maze, self.moves

    def pickDirection(self):
        choices = self.getPaths()

        if choices > 1:
            self.oops_index = len(self.moves) - 1
        elif choices == 0:
            self.wipe()

        return self.paths.pop()

    def wipe(self):
        """
        Remove bread crumbs from dead end moves
        :return:
        """
        for idx in range(len(self.moves) - 1, self.oops_index, -1):
            self.setMazeLocMark(self.moves[idx], Maze.PATH)

    def takeAStep(self, dir):
        self.current = dir;

    def getPaths(self):
        count = 0
        mark = self.get_path_up()
        if mark == Maze.PATH or mark == Maze.EXIT:
            self.paths.push(Location(self.current.row - 1, self.current.col))
            count += 1

        mark = self.get_path_right()
        if mark == Maze.PATH or mark == Maze.EXIT:
            self.paths.push(Location(self.current.row, self.current.col + 1))
            count += 1

        mark = self.get_path_down()
        if mark == Maze.PATH or mark == Maze.EXIT:
            self.paths.push(Location(self.current.row + 1, self.current.col))
            count += 1

        mark = self.get_path_left()
        if mark == Maze.PATH or mark == Maze.EXIT:
            self.paths.push(Location(self.current.row, self.current.col - 1))
            count += 1

        return count

    def get_path_up(self):
        return self.getMazeLocMark(Location(self.current.row - 1, self.current.col))

    def get_path_right(self):
        return self.getMazeLocMark(Location(self.current.row, self.current.col + 1))

    def get_path_down(self):
        return self.getMazeLocMark(Location(self.current.row + 1, self.current.col))

    def get_path_left(self):
        return self.getMazeLocMark(Location(self.current.row, self.current.col - 1))

    def dropBC(self):
        self.setMazeLocMark(self.current, Maze.BREAD)

    def setMazeLocMark(self, spot, mark):
        self.maze[spot.row][spot.col] = mark

    def getMazeLocMark(self, spot):
        #print(spot.getRow(), spot.getCol())
        return self.maze[spot.getRow()][spot.getCol()]

    def __str__(self):
        return str(self.maze)