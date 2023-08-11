Design


Step 1: Manual process to demonstrate concepts


![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Breadth%20First%20Search/Maze/img/4.png)
```
Visited: 0 
         0
Queue: 

Visited: 0 
         1
Queue:   0
1. Add 0 to the queue
2. Mark 0 as visited

Visited: 0
         1
Queue: 
1. Remove 0 from the queue
2. Print 0

Visited: 0 C K
         1 1 1
Queue:  C K
1. Add C and K to the queue
2. Mark C and K as visited

Visited: 0 C K
         1 1 1
Queue:  K
1. Remove C from the queue
2. Print 0 C

Visited: 0 C K G 
         1 1 1 1
Queue:  K G
1. Add G to the queue
2. Mark G as visited

Visited: 0 C K G
         1 1 1 1
Queue: G
1. Remove K from the queue
2. Print: 0 C K


Visited: 0 C K G 
         1 1 1 1
Queue: 
1. Remove G from the queue
2. Print 0 C K G

Visited: 0 C K G D
         1 1 1 1 1
Queue: D
1. Add D to the queue
2. Mark D as visited

Visited: 0 C K G D
         1 1 1 1 1
Queue:
1. Remove D from the queue
2. Print: 0 C K G D

Visited: 0 C K G D A I
         1 1 1 1 1 1 1
Queue: A I
1. Add A, I to the queue
2. Mark A, I as visited

Visited: 0 C K G D A I
         1 1 1 1 1 1 1
Queue: I
1. Remove A from the queue
2. Print: 0 C K G D A

Visited: 0 C K G D A I B
         1 1 1 1 1 1 1 1
Queue: I B
1. Add B to the queue
2. Mark B as visited

Visited: 0 C K G D A I B
         1 1 1 1 1 1 1 1
Queue: B
1. Remove I from the queue
2. Print: 0 C K G D A I

Visited: 0 C K G D A I B
         1 1 1 1 1 1 1 1
Queue: B
1. Remove I from the queue
2. Print: 0 C K G D A I

Visited: 0 C K G D A I B U
         1 1 1 1 1 1 1 1 1
Queue: B U
1. Add U to the queue
2. Mark U as visited

Visited: 0 C K G D A I B U
         1 1 1 1 1 1 1 1 1
Queue: U
1. Remove B from the queue
2. Print 0 C K G D A I B

Visited: 0 C K G D A I B U
         1 1 1 1 1 1 1 1 1
Queue: 
1. Remove U from the queue
2. Print 0 C K G D A I B U

So reach R.
```

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

![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Breadth%20First%20Search/Maze/img/1.png)
![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Breadth%20First%20Search/Maze/img/2.png)
