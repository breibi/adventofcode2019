def param_mode(input, value, i):  # i: param index 0...n
    p = (value - value % 10**(2+i)) / 10**(2+i)
    return p % 10

def param_value(input, i, param_idx):
    m = param_mode(input, input[i],param_idx)
    if m == 0:
        return input[input[i+1+param_idx]]
    else:
        return input[i+1+param_idx]


def int_computer(input, pos, input_values):

    finished = False
    i = pos
    while not finished:
        action = input[i] % 100

        if action in [1,2,7,8]:
            a = param_value(input, i, 0)
            b = param_value(input, i, 1)
            j = input[i + 3]
            inc = 4
        elif action in [5,6]:
            a = param_value(input, i,0)
            b = param_value(input, i,1)
            inc = 3
        else:
            j = input[i + 1]
            inc = 2

        if action == 1:
            input[j] = a+b
        elif action == 2:
            input[j] = a*b
        elif action == 3:
            input[j] = input_values[0]
            input_values.pop(0)
        elif action == 4:
            i += inc
            return input[j], i
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



settings = {5, 6, 7, 8, 9}
combinations = []
for a in settings:
    for b in settings.difference({a}):
        for c in settings.difference({a,b}):
            for d in settings.difference({a,b,c}):
                for e in settings.difference({a,b,c,d}):
                    combinations.append([a,b,c,d,e])


thruster = []

for [a,b,c,d,e] in combinations:
    out = 0
    pos_a = pos_b = pos_c = pos_d = pos_e = 0
    with open("dec07.txt") as f:
        s = f.read()
        inputa = [int(x) for x in s.split(",")]
        inputb = [int(x) for x in s.split(",")]
        inputc = [int(x) for x in s.split(",")]
        inputd = [int(x) for x in s.split(",")]
        inpute = [int(x) for x in s.split(",")]

    try:
        out, pos_a = int_computer(inputa, pos_a, [a, out])
        out, pos_b = int_computer(inputb, pos_b, [b, out])
        out, pos_c = int_computer(inputc, pos_c, [c, out])
        out, pos_d = int_computer(inputd, pos_d, [d, out])
        out, pos_e = int_computer(inpute, pos_e, [e, out])

        while True:
            out, pos_a = int_computer(inputa, pos_a, [out])
            out, pos_b = int_computer(inputb, pos_b, [out])
            out, pos_c = int_computer(inputc, pos_c, [out])
            out, pos_d = int_computer(inputd, pos_d, [out])
            out, pos_e = int_computer(inpute, pos_e, [out])
    except:
        thruster.append(out)

print(max(thruster))