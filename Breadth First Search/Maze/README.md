Design


Step 1: Manual process to demonstrate concepts


![image](https://github.com/ceciliazhao1/Algorithm/tree/main/Breadth%20First%20Search/Maze/img/4.png)


Step 2: Implement
"How to use Breadth-First Traversal approach to implement a Python code to solve the LeetCode question: '490. The Maze', with the test data: 'Input: maze = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]], start =[0,4], destination = [4,4]; Output: true'"

```
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

# Test data
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

result = hasPath(maze, start, destination)
print(result)  # Output: True

```

![image](https://github.com/ceciliazhao1/Algorithm/tree/main/Breadth%20First%20Search/Maze/img/1.png)
![image](https://github.com/ceciliazhao1/Algorithm/tree/main/Breadth%20First%20Search/Maze/img/2.png)
