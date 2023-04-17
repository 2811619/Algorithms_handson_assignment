from collections import deque

# To keep track of the blocks of maze
class Maze_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Each block will have its own position and cost of steps taken
class Node:
    def __init__(self, position: Maze_Position, cost):
        self.position = position
        self.cost = cost
    
def bfs(maze, start_x, start_y, end_x, end_y):
    #return -1 if path does not exists
    # otherwise return cost the shortest path

    # To get neighbours of current node
    adjacent_cell_x = [1, 0, 0, -1]
    adjacent_cell_y = [0, 1, -1, 0]

    # To keep track of the maze position from start to end
    destination = Maze_Position(end_x, end_y)
    start = Maze_Position(start_x, start_y)

    # Getting the length of the 2D array 
    r, c = (len(maze), len(maze))

    # Making all as a non visited blocks
    visited_blocks = [[False for i in range(r)]
                for j in range(c)]

    # Assigning start position of visited_blocks as true
    visited_blocks[start.x][start.y] = True

    # Created queue to keep track of the visited nodes while exploring other nodes
    queue = deque()
    solution = Node(start, 0)
    queue.append(solution)
    cells = 4
    cost = 0

    # Visit the Node and push into Queue
    while queue:
        current_block = queue.popleft()  # Dequeue the front cell
        current_position = current_block.position

        # If the current position matches the destination, it will print the cost taken to reach the destination
        if current_position.x == destination.x and current_position.y == destination.y:
            print("BFS")
            return current_block.cost
        
        if current_block not in visited_blocks:
            visited_blocks[current_position.x][current_position.y] = True
            cost = cost + 1
        x_position = current_position.x
        y_position = current_position.y

        # By using the cells count 4, It will iterate the adjacents and found the x_position and y_position positions in the maze
        for i in range(cells):
            if x_position == len(maze) - 1 and adjacent_cell_x[i] == 1:
                x_position = current_position.x
                y_position = current_position.y + adjacent_cell_y[i]
            if y_position == 0 and adjacent_cell_y[i] == -1:
                x_position = current_position.x + adjacent_cell_x[i]
                y_position = current_position.y
            else:
                x_position = current_position.x + adjacent_cell_x[i]
                y_position = current_position.y + adjacent_cell_y[i]

            # The written positions are matched here and if it's equal 1 it will make as the visited block true and increment the cost
            if x_position < 12 and y_position < 12 and x_position >= 0 and y_position >= 0:
                if maze[x_position][y_position] == 1:
                    if not visited_blocks[x_position][y_position]:
                        next_cell = Node(Maze_Position(x_position, y_position),
                                       current_block.cost + 1)
                        visited_blocks[x_position][y_position] = True
                        queue.append(next_cell)
    return -1

def create_node(x, y, c):
    val = Maze_Position(x, y)
    return Node(val, c + 1)

def dfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return steps with backtracking

    # To get neighbours of current node
    adjacent_cell_x = [1, 0, 0, -1]
    adjacent_cell_y = [0, 1, -1, 0]

    # to keep track of the maze position from start to end
    destination = Maze_Position(end_x, end_y)
    start = Maze_Position(start_x, start_y)

    # Getting the length of the 2D array 
    r, c = (len(maze), len(maze))

    # Making all as a non visited blocks
    visited_blocks = [[False for i in range(r)]
               for j in range(c)]
    visited_blocks[start.x][start.y] = True

    # Created stack to keep track of the visited nodes while exploring other nodes
    stack = deque()
    solution = Node(start, 0)
    stack.append(solution)
    neigh = 4
    neighbours = []
    cost = 0

    # Visit that Node and push into Stack
    while stack:
        current_block = stack.pop()
        current_position = current_block.position
        
        # If the current position matches the destination, it will print the cost taken to reach the destination
        if current_position.x == destination.x and current_position.y == destination.y:
            print("DFS")
            return current_block.cost
        x_position = current_position.x
        y_position = current_position.y

        # By using the cells count 4, It will iterate the adjacents and found the x_position and y_position positions in the maze
        for i in range(neigh):
            if x_position == len(maze) - 1 and adjacent_cell_x[i] == 1:
                x_position = current_position.x
                y_position = current_position.y + adjacent_cell_y[i]
            if y_position == 0 and adjacent_cell_y[i] == -1:
                x_position = current_position.x + adjacent_cell_x[i]
                y_position = current_position.y
            else:
                x_position = current_position.x + adjacent_cell_x[i]
                y_position = current_position.y + adjacent_cell_y[i]

            # The written positions are matched here and if it's equal 1 it will make as the visited block true and increment the cost
            if x_position != 12 and x_position != -1 and y_position != 12 and y_position != -1:
                if maze[x_position][y_position] == 1:
                    if not visited_blocks[x_position][y_position]:
                        cost += 1
                        visited_blocks[x_position][y_position] = True
                        stack.append(create_node(x_position, y_position, current_block.cost))
    return -1


def main():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],   
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    end_x, end_y = 10, 0
    start_x, start_y = 3, 11
    bfs_res = bfs(maze, start_x, start_y, end_x, end_y)
    if bfs_res != -1:
        print("Shortest cost = ", bfs_res)
    else:
        print("Path does not exit")

    print()
    
    dfs_res = dfs(maze, start_x, start_y, end_x, end_y)
    if dfs_res != -1:
        print("Shortest cost = ", dfs_res)
    else:
        print("Path does not exit")

if __name__ == '__main__':
    main()