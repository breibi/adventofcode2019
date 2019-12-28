from collections import defaultdict

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

class Intcomputer:
    def __init__(self, program, pos):
        self._program = program
        self._pos = pos
        self._base = 0


    @classmethod
    def fromFile(cls, filename):
        with open(filename) as f:
            s = f.read()

            program = defaultdict(int)
            lst = s.split(",")
            for i in range(0, len(lst)):
                program[i] = int(lst[i])
            return cls(program, 0)


    def process(self, inputs):
        finished = False

        while not finished:
            action = self._program[self._pos] % 100

            if action in [1, 2, 7, 8]:  # add, multiply, 7=less than, 8=equals
                a = param_value(self._program, self._pos, 0, self._base)
                b = param_value(self._program, self._pos, 1, self._base)
                j = param_pos(self._program, self._pos, 2, self._base)

                inc = 4
            elif action in [5, 6]:  # 5=jump-if-true, 6=jump-if-false
                a = param_value(self._program, self._pos, 0, self._base)
                b = param_value(self._program, self._pos, 1, self._base)
                inc = 3
            elif action in [3, 4, 9, 99]:  # 3=input, 4=output, 9=adjust relative base, 99=stop
                j = param_pos(self._program, self._pos, 0, self._base)
                inc = 2
            else:
                print("something wrong 2")
                quit()

            if action == 1:
                self._program[j] = a + b
            elif action == 2:
                self._program[j] = a * b
            elif action == 3:
                self._program[j] = inputs[0]
                inputs.pop(0)
            elif action == 4:
                #  print(input[j])
                self._pos += inc
                return self._program[j], False
            elif action == 5:
                if a != 0:
                    self._pos = b
                    inc = 0
            elif action == 6:
                if a == 0:
                    self._pos = b
                    inc = 0
            elif action == 7:
                if a < b:
                    self._program[j] = 1
                else:
                    self._program[j] = 0
            elif action == 8:
                if a == b:
                    self._program[j] = 1
                else:
                    self._program[j] = 0
            elif action == 9:
                self._base += self._program[j]
            elif action == 99:
                return -1, True
            else:
                print("something wrong")
                quit()
            self._pos += inc


class Intcomputer2:
    def __init__(self, program, pos):
        self._program = program
        self._pos = pos
        self._base = 0

    @classmethod
    def fromFile(cls, filename):
        with open(filename) as f:
            s = f.read()

            program = defaultdict(int)
            lst = s.split(",")
            for i in range(0, len(lst)):
                program[i] = int(lst[i])
            return cls(program, 0)

    def process(self, inputs):
        finished = False

        while not finished:
            action = self._program[self._pos] % 100

            if action in [1, 2, 7, 8]:  # add, multiply, 7=less than, 8=equals
                a = param_value(self._program, self._pos, 0, self._base)
                b = param_value(self._program, self._pos, 1, self._base)
                j = param_pos(self._program, self._pos, 2, self._base)

                inc = 4
            elif action in [5, 6]:  # 5=jump-if-true, 6=jump-if-false
                a = param_value(self._program, self._pos, 0, self._base)
                b = param_value(self._program, self._pos, 1, self._base)
                inc = 3
            elif action in [3, 4, 9, 99]:  # 3=input, 4=output, 9=adjust relative base, 99=stop
                j = param_pos(self._program, self._pos, 0, self._base)
                inc = 2
            else:
                print("something wrong 2")
                quit()

            if action == 1:
                self._program[j] = a + b
            elif action == 2:
                self._program[j] = a * b
            elif action == 3:
                if len(inputs) > 0:
                    self._program[j] = inputs[0]
                    inputs.pop(0)
                else:
                    return None, False
            elif action == 4:
                print(chr(self._program[j]))
               # self._pos += inc
                #return self._program[j], False
            elif action == 5:
                if a != 0:
                    self._pos = b
                    inc = 0
            elif action == 6:
                if a == 0:
                    self._pos = b
                    inc = 0
            elif action == 7:
                if a < b:
                    self._program[j] = 1
                else:
                    self._program[j] = 0
            elif action == 8:
                if a == b:
                    self._program[j] = 1
                else:
                    self._program[j] = 0
            elif action == 9:
                self._base += self._program[j]
            elif action == 99:
                return -1, True
            else:
                print("something wrong")
                quit()
            self._pos += inc
#
#
# with open("dec09.txt") as f:
#     s = f.read()
#     lst = s.split(",")
#     myprogram = defaultdict(int)
#
#
#     for i in range(0, len(lst)):
#         myprogram[i] = int(lst[i])

# comp = Intcomputer(myprogram, 0)
#
# out, finished = comp.process([1])
# print(out)
# while not finished:
#     out, finished = comp.process([out])
#     print(out)
#
#
# with open("dec09.txt") as f:
#     s = f.read()
#     lst = s.split(",")
#     myprogram = defaultdict(int)
#
#
#     for i in range(0, len(lst)):
#         myprogram[i] = int(lst[i])
#
# comp = Intcomputer.fromFile("dec09.txt")
# out, finished = comp.process([2])
# print(out)
# while not finished:
#     out, finished = comp.process([out])
#     print(out)


