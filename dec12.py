import numpy as np

pos1 = np.array([-7, -8, 9])
pos2 = np.array([-12, -3, -4])
pos3 = np.array([6, -17, -9])
pos4 = np.array([4, -10, -6])

positions = [pos1, pos2, pos3, pos4]
velocities = [np.array([0,0,0]) for _ in range(0,4)]

for time in range(0,1000):
    for i in range(0, 3):
        for j in range(i+1, 4):
            diff = np.subtract(positions[j],positions[i])
            s = np.sign(diff)
            velocities[i] += s
            velocities[j] -= s

    for i in range(0,4):
        positions[i] += velocities[i]

print(positions)
print(velocities)


potential = [sum(x) for x in np.abs(positions)]
kinetic = [sum(x) for x in np.abs(velocities)]
result = sum([p*k for (p,k) in zip(potential, kinetic)])
print(result)
