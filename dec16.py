base_pattern = [0, 1, 0, -1]


def get_pattern(pos):
    lst = []
    for i in base_pattern:
        for j in range(0,pos+1):
            lst.append(i)

    return lst

def fft(input):   # "flawed frequency transmission"
    result = ""
    for i in range(0, len(input)):
        pattern = get_pattern(i)
        pos = 1
        sum = 0
        for j in range(0, len(input)):
            sum += int(input[j]) * pattern[pos]
            pos = (pos+1) % len(pattern)
        result = result + str(sum)[-1]
    return result


with open("dec16.txt") as f:
    input = f.read()

offset = 0 # part one
#offset = int(input[:7])  # part two offset=5976463

for phase in range(0,100):
    input = fft(input)

print(input[offset:offset+8])
