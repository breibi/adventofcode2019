from intcode import Intcomputer
from collections import defaultdict

# part one
painted_panels = defaultdict(int)
painted_panels[(0,0)] = 0

pos = (0,0)
dir = (0,1)

comp = Intcomputer.fromFile("dec11.txt")
finished = False
while not finished:
    old_col = painted_panels[pos]
    new_col, finished = comp.process([old_col])
    painted_panels[pos] = new_col

    rotation, finished = comp.process([new_col])
    if rotation == 0:  # turn left
        dir = (-dir[1], dir[0])
    else:
        dir = (dir[1], -dir[0])

    pos = (pos[0]+dir[0], pos[1]+dir[1])

print(len(painted_panels))

# part two
painted_panels = defaultdict(int)
painted_panels[(0,0)] = 1

pos = (0,0)
dir = (0,1)
comp = Intcomputer.fromFile("dec11.txt")
finished = False
while not finished:
    old_col = painted_panels[pos]
    new_col, finished = comp.process([old_col])
    painted_panels[pos] = new_col

    rotation, finished = comp.process([new_col])
    if rotation == 0:  # turn left
        dir = (-dir[1], dir[0])
    else:
        dir = (dir[1], -dir[0])

    pos = (pos[0]+dir[0], pos[1]+dir[1])

xs = [x for (x,y) in painted_panels.keys()]
ys = [y for (x,y) in painted_panels.keys()]

minx = min(xs)
maxx = max(xs)
miny = min(ys)
maxy = max(ys)

for y in range(maxy+1, miny-1, -1):
    for x in range(minx-1, maxx+1):
        if painted_panels[(x,y)] == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print("")
