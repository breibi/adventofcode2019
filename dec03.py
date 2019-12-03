def dist(p1, p2):
    return(abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))

def dist_0(p):
    return dist((0,0), p)

with open("dec03.txt") as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")

offset = {'U': [0, 1], 'D':  [0, -1], 'L':  [1, 0], 'R': [-1, 0]}
points = set()
current = (0,0)
steps = 0
intersec_steps = {}
for line in wire1:
    dir = line[0]
    length = int(line[1:])

    for i in range(0, length):
        steps += 1
        new_point = (current[0] + offset[dir][0], current[1]+ offset[dir][1])
        points.add(new_point)
        if new_point not in intersec_steps:
            intersec_steps[new_point] = steps
        current = new_point

current = (0,0)
intersections = []

min_steps = steps
steps = 0

for line in wire2:
    dir = line[0]
    length = int(line[1:])

    for i in range(0, length):
        steps += 1
        new_point = (current[0] + offset[dir][0], current[1] + offset[dir][1])
        if new_point in points:
            intersections.append(new_point)

            if steps + intersec_steps[new_point] < min_steps:
                min_steps = steps + intersec_steps[new_point]

        current = new_point

p = min(intersections, key=dist_0)
print(p)
print(dist_0(p))
print(min_steps)