def bfs(tree, start_node, goal_node):
    visited = [start_node]
    queue = [start_node]
    while len(queue) > 0:
        node = queue.pop()
        if node == goal_node:
            return True
        for child in tree[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)
    return False


n = int(input())

commands = [input() for i in range(n)]

current_tree = dict()

for command in commands:
    command_lst = command.split()
    current_tree.update({command_lst[0]: command_lst[2:]})

n = int(input())

commands = [input() for i in range(n)]

result = set()

for i in range(1, len(commands)):
    for j in range(i):
        if bfs(current_tree, commands[i], commands[j]):
            result.add(commands[i])

for command in commands:
    if command in result:
        print(command)
