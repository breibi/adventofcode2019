from intcode import Intcomputer
import numpy as np

comp = Intcomputer.fromFile("dec17.txt")

finished = False
grid = [[]]
j = 0
i = 0
while not finished:
    out, finished = comp.process([])
    if finished:
        break
    print(chr(out), end='')

    if out == 10:
        j += 1
        i = 0
    elif out == 35:
        if len(grid)-1 < j:
            grid.append([])
        grid[j].append(1)
        i += 1
    elif out == 46:
        if len(grid)-1 < j:
            grid.append([])
        grid[j].append(0)
        i += 1
    else:
        if len(grid)-1 < j:
            grid.append([])
        grid[j].append(-1)
        start = np.array([i,j])
        i += 1

for line in grid:
    print(*line)

up = np.array([0,-1])
down = np.array([0,1])
left = np.array([-1,0])
right = np.array([1,0])

grid = np.array(grid)

pattern = [[0, 1, 0],
           [1, 1, 1],
           [0, 1, 0]]
cnt = 0
sum = 0
for y in range(0, grid.shape[0]-2):
    for x in range(0, grid.shape[1]-2):
        if np.array_equal(grid[y:y+3, x:x+3], pattern):
            cnt += 1
            sum += (y+1)*(x+1)

print("nr of intersections: ", cnt)
print(sum)
