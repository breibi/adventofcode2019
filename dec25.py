from intcode import Intcomputer
from itertools import product

comm_list = ['west', 'take hypercube', 'west', 'take space law space brochure', 'west', 'north', 'take shell',
             'west', 'take mug', 'south', 'take festive hat', 'north', 'east', 'south', 'east', 'east', 'east',
             'south', 'east', 'take boulder', 'west', 'north', 'east', 'north', 'north', 'west', 'north',
             'take whirled peas', 'west', 'west', 'take astronaut ice cream', 'south', 'south']

drop_commands = ['drop space law space brochure', 'drop boulder', 'drop whirled peas','drop hypercube',
                 'drop astronaut ice cream', 'drop festive hat', 'drop shell', 'drop mug']

take_commands = ['take hypercube', 'take space law space brochure', 'take boulder', 'take astronaut ice cream',
                 'take whirled peas', 'take festive hat', 'take shell', 'take mug']


comp = Intcomputer.fromFile("dec25.txt")
finished = False
input_commands = []
message = ""

# try all combinations of items to achieve the right weight
combinations = list(product([True, False], repeat=8))

while not finished:
    out, finished = comp.process(input_commands)
    if (out is not None) and (out > 0):
        message += chr(out)
    if message.endswith("Command?"):
        #print(message)

        if len(comm_list) == 0:
            print(message)
            
            comm_list = take_commands.copy()  # take all items
            c = combinations[0]

            for i, drop in enumerate(c):     # drop some of the items
                if drop:
                    comm_list.append(drop_commands[i])
            comm_list.append('south')
            command = comm_list[0]
            comm_list.pop(0)
            combinations.pop(0)
            #command = input("Enter Command")
        else:
            command = comm_list[0]
            comm_list.pop(0)

        input_commands = []
        for c in command:
            input_commands.append(ord(c))
        input_commands.append(10)
        message = ""

print(message)

