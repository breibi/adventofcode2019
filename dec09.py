from collections import  defaultdict

def param_mode(input, value, i):  # i: param index 0...n
    p = (value - value % 10**(2+i)) / 10**(2+i)
    return p % 10

def param_value(input, i, param_idx, base):
    m = param_mode(input, input[i],param_idx)
    if m == 0:
        return input[input[i+1+param_idx]]
    elif m == 1:
        return input[i+1+param_idx]
    elif m == 2:
        return input[input[i+1+param_idx]+base]
    else:
        print("nochwas falsch")

def param_pos(input, i, param_idx, base):
    m = param_mode(input, input[i],param_idx)
    if m == 0:
        return input[i+1+param_idx]
    elif m == 1:
        return i+1+param_idx
    elif m == 2:
        return input[i+1+param_idx]+base
    else:
        print("nochwas falsch")


def int_computer(input, pos, input_values, base):

    finished = False
    i = pos
    while not finished:
        action = input[i] % 100

        if action in [1,2,7,8]:  # add, multiply, 7=less than, 8=equals
            a = param_value(input, i, 0, base)
            b = param_value(input, i, 1, base)
            j = param_pos(input, i, 2, base)

            inc = 4
        elif action in [5,6]:  # 5=jump-if-true, 6=jump-if-false
            a = param_value(input, i,0, base)
            b = param_value(input, i,1, base)
            inc = 3
        elif action in [3,4,9,99]:  # 3=input, 4=output, 9=adjust relative base, 99=stop
           # j = param_value(input, i, 0, base)
           #  if param_mode(input, input[i], 0) == 2:
           #      j = input[i+1]+base
           #  elif param_mode(input, input[i], 0) == 1:
           #      j = i+1
           #  else:
           #      j = input[i + 1]
           j = param_pos(input, i, 0, base)
           inc = 2
        else:
            print("something wrong 2")
            quit()

       # if j not in input:
        #    input[j] = 0
      #  if j >= len(input):
       #     input.append([0 for _ in range(len(input), j)])

        if action == 1:
            input[j] = a+b
        elif action == 2:
            input[j] = a*b
        elif action == 3:
            input[j] = input_values[0]
            input_values.pop(0)
        elif action == 4:
         #   i += inc
            print(input[j])
          #  return input[j], i
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
                input[j] = 1
            else:
                input[j] = 0
        elif action == 8:
            if a == b:
                input[j] = 1
            else:
                input[j] = 0
        elif action == 9:
            base += input[j]
        elif action == 99:
            finished = True
        else:
            print("something wrong")
            quit()
        i += inc
       # if i >= max(input.keys()):
        #    finished = True

with open("dec09.txt") as f:
    s = f.read()
    lst = s.split(",")
    input = defaultdict(int)


    for i in range(0, len(lst)):
        input[i] = int(lst[i])
    #input = [int(x) for x in s.spl)it(",")]

int_computer(input, 0, [2], 0)


