import numpy as np


with open("dec10.txt") as f:
    asteroids = []
    y = 0
    for line in f:
        for a in [(x,y) for x in range(0, len(line)) if line[x] == '#']:
            asteroids.append(a)
        y += 1

print(asteroids)
detected = [set() for _ in asteroids]

for i,loc in enumerate(asteroids):
    for j, a in enumerate(asteroids):
        if a != loc:
            dx = a[0]-loc[0]
            dy = -a[1]+loc[1]
            dist = abs(dx) + abs(dy)

            angle = np.arctan2(dy,dx)
            if angle < 0:
                angle += 2*np.pi

            detected[i].add((angle, dist, j))


angles = [{a for (a,d, i) in lst} for lst in detected]
lengths = [len(angle_list) for angle_list in angles]
i = lengths.index(max(lengths))
print(i)
print(asteroids[i])
print("solution 1: ", lengths[i])

print(detected[i])
clockwise = [((np.pi/2-a+2*np.pi)%(2*np.pi), d, j) for (a,d,j) in detected[i]]
print(clockwise)

clockwise = sorted(clockwise)
print(clockwise)

clockwise = [[a,d,j] for (a,d,j) in clockwise]

for j in range(0, len(clockwise)-1):
    k = 1
    while clockwise[j+k][0] == clockwise[j][0]:
        clockwise[j+k][0] += 2*np.pi*k
        k += 1
print(clockwise)

clockwise = sorted(clockwise, key = lambda x: x[0])
print(clockwise)

print(clockwise[199])
print("solution 2: ", asteroids[clockwise[199][2]])

