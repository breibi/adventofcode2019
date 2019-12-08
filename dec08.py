with open("dec08.txt") as f:
    a = f.read(25*6)
    input = []
    while a != "":
        input.append(a)
        a = f.read(25*6)

zeros = [s.count('0') for s in input]
ones = [s.count('1') for s in input]
twos = [s.count('2') for s in input]

i = zeros.index(min(zeros))
print(ones[i] * twos[i])


# part two

image = [[2 for i in range(0,25)] for j in range(0,6)]

# for i in range(0,6):
#     for j in range(0,25):
#         val = 3
#         for n in range(0,len(input)):
#             next_val = int(input[n][i*25+j])
#             if next_val <= val:
#                 val = next_val
#             else:
#                 break
#
#         image[i][j] = val

for n in range(0, len(input)):
    for i in range(0, 6):
        for j in range(0, 25):
            if image[i][j] == 2:
                image[i][j] = int(input[n][i*25+j])
          #  if val < image[i][j]:
           #     image[i][j] = val

for line in image:
    print(line)

for line in image:
    s = str(line).replace('0', ' ')
    s = s.replace(',', '')
    s = ""
    s = s.join([str(i) for i in line])
    s = s.replace("0", ' ')
    s = s.replace("1", "X")
    print(str(s))
   # print(*line, sep="")


