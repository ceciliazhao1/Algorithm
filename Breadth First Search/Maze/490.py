from collections import deque

def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([start])
    visited = set()

    while queue:
        row, col = queue.popleft()
        if [row, col] == destination:
            return True
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in directions:
            newRow, newCol = row, col
            while 0 <= newRow + dr < rows and 0 <= newCol + dc < cols and maze[newRow + dr][newCol + dc] == 0:
                newRow += dr
                newCol += dc
            queue.append((newRow, newCol))
    return False

maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
result = hasPath(maze, start, destination)
print(result)  # Output: True
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]
result = hasPath(maze, start, destination)
print(result)  # Output: False
maze = [[0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]

result = hasPath(maze, start, destination)
print(result)  # Output: False



