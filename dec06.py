with open("dec06.txt") as f:
    input = {}
    for line in f:
        a,b = line.rstrip("\n").split(")")
        if a in input:
            input[a].append(b)
        else:
            input[a] = [b]

print(input)

def build_tree1(input, node_id, node_level):
    sum = 0

    if node_id in input:
        for child_node in input[node_id]:
            sum += node_level + build_tree1(input, child_node, node_level+1)

    return sum

def build_tree2(input, node_id, path, target_node):
    my_path = path.copy()
    my_path.append(node_id)
    if node_id == target_node:
        return my_path

    if node_id in input:
        for child_node in input[node_id]:
            sub_path = build_tree2(input, child_node, my_path, target_node)
            if sub_path != None:
                return sub_path

    return None


# part one
print(build_tree1(input, 'COM', 1))

# part two
path1 = build_tree2(input, 'COM', [], 'YOU')
path2 = build_tree2(input, 'COM', [], 'SAN')

path1.reverse()
path2.reverse()

i = 1
while True:
    if path1[i] in path2:
        result = i-1 + path2.index(path1[i])-1
        break
    i += 1

print(result)





