from location import Location
from stack import Stack

class Maze():
    bread = 'B'
    exit = 'X'
    wall = '1'
    path = '0'

    def __init__(self, fileName):
        file = open(fileName, "r")
        self.maze = file.read().split("\n")
        self.current = Location(1,0)
        self.paths = Stack()

    def solve_it(self):
        self.dropBC()
        self.current.moveRight()

        while self.getMazeLocMark(self.current) != Maze.exit:
            self.takeAStep(dir)

    def pickDirection(self):
        self.getPaths()

    def takeAStep(self, dir):
        pass

    def getPaths(self):
        row = self.current.row
        col = self.current.col
        if self.getMazeLocMark(Location(row + 1, col)) == Maze.path:
            self.paths.push(Location(row + 1, col))
        if self.getMazeLocMark(Location(row - 1, col)) == Maze.path:
            self.paths.push(Location(row - 1, col))
        if self.getMazeLocMark(Location(row, col + 1)) == Maze.path:
            self.paths.push(Location(row, col + 1))
        if self.getMazeLocMark(Location(row, col - 1)) == Maze.path:
            self.paths.push(Location(row, col - 1))


    def dropBC(self):
        self.setMazeLocMark(self.current, Maze.bread)

    def setMazeLocMark(self, spot, mark):
        self.maze[spot.row][spot.col] = mark

    def getMazeLocMark(self, spot):
        return self.maze[spot.getRow()][spot.getCol()]

    def __str__(self):
        return str(self.maze)