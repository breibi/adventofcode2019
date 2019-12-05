with open("dec05.txt") as f:
    input = [int(x) for x in f.read().split(",")]

# part one
system_id = 1

# part two
system_id = 5

def param_mode(value, i):  # i: param index 0...n
    p = (value - value % 10**(2+i)) / 10**(2+i)
    return p % 10

def param_value(i, param_idx):
    m = param_mode(input[i],param_idx)
    if m == 0:
        return input[input[i+1+param_idx]]
    else:
        return input[i+1+param_idx]

finished = False
i = 0
while not finished:
    action = input[i] % 100

    if action in [1,2,7,8]:
        a = param_value(i, 0)
        b = param_value(i, 1)
        j = input[i + 3]
        inc = 4
    elif action in [5,6]:
        a = param_value(i,0)
        b = param_value(i,1)
        inc = 3
    else:
        j = input[i + 1]
        inc = 2

    if action == 1:
        input[j] = a+b
    elif action == 2:
        input[j] = a*b
    elif action == 3:
        input[j] = system_id
    elif action == 4:
        print(input[j])
    elif action == 5:
        if a != 0:
            i = b
            inc = 0
    elif action == 6:
        if a == 0:
            i = b
            inc = 0
    elif action == 7:
        if a < b:
            input[j] = a
        else:
            input[j] = 0
    elif action == 8:
        if a == b:
            input[j] = a
        else:
            input[j] = 0

    elif action == 99:
        finished = True
    else:
        print("something wrong")
        quit()
    i += inc
    if i >= len(input):
        finished = True


