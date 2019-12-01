with open("dec01.txt") as f:
    input = [int(x) for x in f]

# part one
sum = 0
for n in input:
    sum += n // 3 - 2

print(sum)

# part two
sum = 0
for n in input:
    while n > 8:
        n = n // 3 - 2
        sum += n

print(sum)