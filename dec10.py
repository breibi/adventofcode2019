import numpy as np

with open("dec10_test.txt") as f:
    asteroids = []
    y = 0
    for line in f:
        for a in [(x,y) for x in range(0, len(line)) if line[x] == '#']:
            asteroids.append(a)
        y += 1


print(asteroids)
detected = [set() for _ in asteroids]

for i,loc in enumerate(asteroids):
    for a in asteroids:
        if a != loc:
            dx = a[0]-loc[0]
            dy = a[1]-loc[1]
            if dx != 0:
                direction = dy/dx
            else:
                direction = np.inf * np.sign(dy)
            s = np.sign(dx)
            detected[i].add((direction, s))

print(detected)
lengths = [len(l) for l in detected]
max_len = max(lengths)
i = lengths.index(max_len)
print(i)
print(asteroids[i])
print(max_len)

