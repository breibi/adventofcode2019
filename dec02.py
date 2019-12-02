with open("dec02.txt") as f:
    input = [int(x) for x in f.read().split(",")]


# part one
input[1] = 12
input[2] = 2

finished = False
i = 0
while not finished:
    action = input[i]
    a = input[input[i+1]]
    b = input[input[i+2]]
    j = input[i+3]
    if action == 1:
        input[j] = a+b
    elif action == 2:
        input[j] = a*b
    elif action == 99:
        finished = True
    else:
        print("something wrong")
        quit()
    i += 4
    if i >= len(input):
        finished = True

print(input[0])

# part two

for noun in range(0,100):
    for verb in range(0,100):

        with open("dec02.txt") as f:
            input = [int(x) for x in f.read().split(",")]

        input[1] = noun
        input[2] = verb

        finished = False
        i = 0
        while not finished:
            action = input[i]
            a = input[input[i+1]]
            b = input[input[i+2]]
            j = input[i+3]
            if action == 1:
                input[j] = a+b
            elif action == 2:
                input[j] = a*b
            elif action == 99:
                finished = True
            else:
                print("something wrong")
                quit()
            i += 4
            if i >= len(input):
                finished = True

        if input[0] == 19690720:
            print(100 * noun + verb)
            print(noun, verb)
            quit()