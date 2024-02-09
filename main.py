class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(node_list):
    if node_list[0] == "":
        return None

    root = Node(node_list[0])
    queue = [root]

    i = 1
    while i < len(node_list):
        current_node = queue.pop(0)

        if node_list[i] != "":
            current_node.left = Node(node_list[i])
            queue.append(current_node.left)
        i += 1

        if i < len(node_list) and node_list[i] != "":
            current_node.right = Node(node_list[i])
            queue.append(current_node.right)
        i += 1

    return root

def find_path(root, target_sum):
    def find_path_recursive(node, target_sum, path, result):
        if node is None:
            return None

        path.append(node.value)

        if node.left is None and node.right is None and int(node.value) == target_sum:
            result.append(path[:])

        find_path_recursive(node.left, target_sum - int(node.value), path, result)
        find_path_recursive(node.right, target_sum - int(node.value), path, result)

        path.pop()

    result = []
    find_path_recursive(root, target_sum, [], result)

    return result

nodes = input("Введите узлы дерева через запятую: ").split(",")
tree = create_tree(nodes)
target_sum = int(input("Введите целевую сумму: "))
paths = find_path(tree, target_sum)

if paths:
    for path in paths:
        print('->'.join(node for node in path))
else:
    print("Подходящего пути не найдено!")