from collections import deque

# To keep track of the blocks of maze
class Maze_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Maze_Position, cost):
        self.pos = pos
        self.cost = cost
    
def bfs(maze, start_x, start_y, end_x, end_y):
    #return -1 if path does not exists
    # otherwise return cost the shortest path

    # To get neighbours of current node
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]

    # To keep track of the maze position from start to end
    dest = Maze_Position(end_x, end_y)
    start = Maze_Position(start_x, start_y)

    # Getting the length of the 2D array 
    m, n = (len(maze), len(maze))

    # Making all as a non visited blocks
    visited_blocks = [[False for i in range(m)]
                for j in range(n)]

    # Assigning start position of visited_blocks as true
    visited_blocks[start.x][start.y] = True

    # Created queue to keep track of the visited nodes while exploring other nodes
    queue = deque()
    sol = Node(start, 0)
    queue.append(sol)
    cells = 4
    cost = 0

    # Visit the Node and push into Queue
    while queue:
        current_block = queue.popleft()  # Dequeue the front cell
        current_pos = current_block.pos

        # If the current position matches the destination, it will print the cost taken to reach the destination
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("BFS")
            # print("Total nodes visited = ", cost)
            return current_block.cost
        
        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1
        x_pos = current_pos.x
        y_pos = current_pos.y

        # By using the cells count 4, It will iterate the adjacents and found the x_pos and y_pos positions in the maze
        for i in range(cells):
            if x_pos == len(maze) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]

            # The written positions are matched here and if it's equal 1 it will make as the visited block true and increment the cost
            if x_pos < 12 and y_pos < 12 and x_pos >= 0 and y_pos >= 0:
                if maze[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        next_cell = Node(Maze_Position(x_pos, y_pos),
                                       current_block.cost + 1)
                        visited_blocks[x_pos][y_pos] = True
                        queue.append(next_cell)
    return -1

def create_node(x, y, c):
    val = Maze_Position(x, y)
    return Node(val, c + 1)

def dfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return steps with backtracking

    # To get neighbours of current node
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]

    # to keep track of the maze position from start to end
    dest = Maze_Position(end_x, end_y)
    start = Maze_Position(start_x, start_y)

    # Getting the length of the 2D array 
    m, n = (len(maze), len(maze))

    # Making all as a non visited blocks
    visited_blocks = [[False for i in range(m)]
               for j in range(n)]
    visited_blocks[start.x][start.y] = True

    # Created stack to keep track of the visited nodes while exploring other nodes
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    neighbours = []
    cost = 0

    # Visit that Node and push into Stack
    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("DFS")
            # print("Total nodes visited = ", cost)
            return current_block.cost
        x_pos = current_pos.x
        y_pos = current_pos.y

        # By using the cells count 4, It will iterate the adjacents and found the x_pos and y_pos positions in the maze
        for i in range(neigh):
            if x_pos == len(maze) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]

            # The written positions are matched here and if it's equal 1 it will make as the visited block true and increment the cost
            if x_pos != 12 and x_pos != -1 and y_pos != 12 and y_pos != -1:
                if maze[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(create_node(x_pos, y_pos, current_block.cost))
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