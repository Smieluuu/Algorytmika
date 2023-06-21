from collections import defaultdict

def rotate_domino(domino):
    return domino[::-1]

def check_is_graph_eulerian(dominos):
    odd_number_of_connections = 0
    for domino in dominos.items():
        if len(domino[1]) % 2 != 0:
            odd_number_of_connections += 1 
    if odd_number_of_connections > 2:
        return False
    return True

def dominos_min_connections(dominos):
    dominos = dominos.items()
    dominos = sorted(dominos, key=lambda x: len(x[1]))
    return dict(dominos)

def find_eulerian_path(graph):
    start_vertex = None
    for vertex, connections in graph.items():
        if len(connections) % 2 != 0:
            start_vertex = vertex
            break
    if start_vertex is None:
        start_vertex = list(graph.keys())[0]

    path = []
    stack = [(start_vertex, graph[start_vertex])]

    while stack:
        vertex, connections = stack[-1]

        if connections:
            next_vertex = connections.pop(0)
            stack.append((next_vertex, graph[next_vertex]))
        else:
            path.append(stack.pop())

    eulerian_path = []
    for i in range(len(path) - 1):
        eulerian_path.append((path[i][0], path[i + 1][0]))
        eulerian_path = eulerian_path[-5:]
    return eulerian_path

def main():
    n = int(input())
    input_dominos_arr = []
    domino_indices = defaultdict(list)  

    for i in range(n):
        domino_block = input().split()
        left, right = int(domino_block[0]), int(domino_block[1])
        input_dominos_arr.append((left, right))
        domino_indices[(left, right)].append(i + 1)  

    dominos_list = defaultdict(list)
    for domino in input_dominos_arr:
        left, right = domino
        dominos_list[left].append(right)
        dominos_list[right].append(left)

    dominos = dominos_min_connections(dominos_list)

    array_of_rotated_dominos = []
    if check_is_graph_eulerian(dominos):
        path = find_eulerian_path(dict(dominos))
        for i in range(len(path)):
            if path[i] not in input_dominos_arr:
                path[i] = rotate_domino(path[i])
                array_of_rotated_dominos.append(path[i])
    else:
        return "No solution"

    for domino in path:
        if domino in array_of_rotated_dominos:
            array_of_rotated_dominos.remove(domino)
            indices = domino_indices[domino]
            index = indices.pop(0)  
            print(index, "-")
        else:
            indices = domino_indices[domino]
            index = indices.pop(0)  
            print(index, "+")
main()