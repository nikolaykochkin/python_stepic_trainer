import json


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


#data = input()
data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'

data = json.loads(data)

current_tree = dict()
result = dict()

for i in data:
    current_tree.update({i['name']: i['parents']})
    result.update({i['name']: 0})

for i in current_tree:
    for j in current_tree:
        if bfs(current_tree, i, j):
            result[j] += 1

for i in sorted(result):
    print(i, ':', result[i])
