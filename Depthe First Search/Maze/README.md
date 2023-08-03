Design


Step 1: Manual process to demonstrate concepts

Step 1.1: Clear Route (Street, Highway)
![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Depthe%20First%20Search/Maze/img/3.jpeg)
![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Depthe%20First%20Search/Maze/img/maze.jpeg)
Step 1.2: Unclear Route (Hotel, Hospital)
![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Depthe%20First%20Search/Maze/img/4.jpeg)
```
Approach : Depth First Search
We can view the given search space in the form of a tree.
The root node of the tree represents the starting position.
Four different routes are possible from each position i.e. right, left, up or down.
1.Start at O, choose right, hit the wall, so choose left, go to C.
2.Start at C, choose right, visited, so choose left, hit the wall, choose up, hit the wall, choose down, go to G.
3.Start at G, choose right, go to H.
4.Start at H, choose right, hit the wall, so choose left, visited, choose up, visited, choose down, go to K.
5.Start at K, choose right, hit the wall, so choose left, hit the wall, choose up, visited, choose down, hit the wall. So go back. (Traversal)
6.Start at G, choose left, go to F.
7.Start at F, choose right, visited, so choose left, go to E.
8.Start at E, choose right, visited, so choose left, go to D.
9.Start at D, choose right, visited, so choose left, hit the wall, choose up, go to A.
10.Start at A, choose right, go to B.
11.Start at B, choose right, hit the wall, so choose left, visited, choose up, hit the wall, choose down, visited. So go back. (Traversal)
12.Start at D, choose down, go to I.
13.Start at I, choose right, go to J.
14.Start at J, choose right, go to U. Find.
```


Step 2: Implement
"How to use Depth-First Traversal approach to implement a Python code to solve the LeetCode question: '490. The Maze', with the test data: 'Input: maze = [[0,0,1,0,0], [0,0,0,0,0], [0,0,0,1,0], [1,1,0,1,1], [0,0,0,0,0]], start =[0,4], destination = [4,4]; Output: true'"

```
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

# Call the function and print the result
print(hasPath(maze, start, destination))  # Output: True
```

![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Depthe%20First%20Search/Maze/img/1.png)
![image](https://github.com/ceciliazhao1/Algorithm/blob/main/Depthe%20First%20Search/Maze/img/2.png)
