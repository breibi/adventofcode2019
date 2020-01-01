# offset is in second half of input length
# -> coefficients are all 1 -> reverse and sum up
def second_half(input, offset):
    result = [input[0]]
    for i in range(1, offset):
        result.append(result[i-1] + input[i])
        result[i] = abs(result[i]) % 10

    return result


with open("dec16.txt") as f:
    input = f.read()

input = input * 10000
arr = [int(c) for c in input]

offset = int(input[:7])  # part two offset=5976463

arr = arr[::-1] #reverse
offset = len(arr)-offset
for phase in range(0,100):
    arr = second_half(arr, offset)

arr = arr[::-1]
print(*arr[0:8])
