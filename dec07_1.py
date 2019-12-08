
def param_mode(input, value, i):  # i: param index 0...n
    p = (value - value % 10**(2+i)) / 10**(2+i)
    return p % 10

def param_value(input, i, param_idx):
    m = param_mode(input, input[i],param_idx)
    if m == 0:
        return input[input[i+1+param_idx]]
    else:
        return input[i+1+param_idx]

def int_computer(input_values):
    with open("dec07.txt") as f:
        input = [int(x) for x in f.read().split(",")]

    finished = False
    i = 0
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
            return input[j]
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


v =[]
settings = {0,1,2,3,4}
for a in settings:
    out_a = int_computer([a,0])
    for b in settings.difference({a}):
        out_b = int_computer([b,out_a])
        for c in settings.difference({a,b}):
            out_c = int_computer([c,out_b])
            for d in settings.difference({a,b,c}):
                out_d = int_computer([d,out_c])
                for e in settings.difference({a,b,c,d}):
                    out_e = int_computer([e,out_d])
                    v.append(out_e)
                    print(out_e, [a,b,c,d,e])

print(max(v))