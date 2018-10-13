import maze, stack, location


m = maze.Maze("maze1.txt")
m, s = m.solve_it()
'''for loc in s:
    print(loc)
'''

for row in m:
    for mark in row:
        print(mark, end='')
    print()



