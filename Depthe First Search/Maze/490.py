def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(x, y):
        if [x, y] == destination:
            return True

        if (x, y) in visited:
            return False

        visited.add((x, y))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            nx, ny = x, y

            # Continue in the current direction until hitting a wall or the boundary of the maze.
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy

            # Recursively explore the new position (nx, ny).
            if dfs(nx, ny):
                return True

        return False

    return dfs(start[0], start[1])

# Test data
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(hasPath(maze, start, destination))  # Output: True

maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]
print(hasPath(maze, start, destination))  # Output: false

maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
start = [4, 3]
destination = [0, 1]
print(hasPath(maze, start, destination))  # Output: false

