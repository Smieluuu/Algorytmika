def main():
    M = int(input())
    tab = []
    for _ in range(M):
        row = input().split()
        tab.append(row)
    start_char = input().strip()
    result = find_longest_path(tab, start_char)
    print(f"The length of the longest path with consecutive characters starting from character {start_char} is {result}")
 
def valid_directions(tab, i, j, dx, dy):
    x, y = i + dx, j + dy
    return 0 <= x < len(tab) and 0 <= y < len(tab[0]) and ord(tab[x][y]) == ord(tab[i][j]) + 1

def explore(tab, i, j, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    max_path_len = 1
    for dx, dy in directions:
        if valid_directions(tab, i, j, dx, dy):
            x, y = i + dx, j + dy
            if (x, y) not in visited:
                visited.add((x, y))
                max_path_len = max(max_path_len, 1 + explore(tab, x, y, visited))
                visited.remove((x, y))
    return max_path_len

def find_longest_path(tab, start_char):
    max_path_len = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == start_char:
                visited = set([(i, j)])
                max_path_len = max(max_path_len, explore(tab, i, j, visited))
    return max_path_len

main()