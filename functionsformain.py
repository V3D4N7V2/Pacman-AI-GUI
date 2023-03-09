# Group 2
# Members:
#  BT19CSE004 Vedant Ghuge
#  BT19CSE082 Yashpal Singh Baghel
#  BT19CSE108 Dushyant Singh
#  BT19ECE036 Vishal Karangale



from commonFunctions import *


def gmA(map, node):
    a = []
    if node[0] > 0:
        if map[node[0] - 1][node[1]] == 0:
            a.append((node[0] - 1, node[1]))
    if node[0] < len(map) - 1:
        if map[node[0] + 1][node[1]] == 0:
            a.append((node[0] + 1, node[1]))
    if node[1] > 0:
        if map[node[0]][node[1] - 1] == 0:
            a.append((node[0], node[1] - 1))
    if node[1] < len(map[0]) - 1:
        if map[node[0]][node[1] + 1] == 0:
            a.append((node[0], node[1] + 1))
    return a


def gmB(map, node):
    a = []
    if node[1] < len(map[0]) - 1:
        if map[node[0]][node[1] + 1] == 0:
            a.append((node[0], node[1] + 1))

    if node[0] > 0:
        if map[node[0] - 1][node[1]] == 0:
            a.append((node[0] - 1, node[1]))

    if node[0] < len(map) - 1:
        if map[node[0] + 1][node[1]] == 0:
            a.append((node[0] + 1, node[1]))

    if node[1] > 0:
        if map[node[0]][node[1] - 1] == 0:
            a.append((node[0], node[1] - 1))

    return a


def bfs(map, start, goal):
    queue = []
    queue.append(start)
    visited = []
    pathFound = dict()
    path = []

    while queue:
        node = queue.pop(0)
        visited.append(node)
        printMap(map, node, goal)
        if node == goal:
            print("Goal Reached")
            print("Path is : ", end=" ")
            while node != start:
                path.append(node)
                node = pathFound[node]

            path.append(start)
            path.reverse()
            print(path)
            printMapPath(map, -1, -1, path)
            return visited, path
        else:

            moves = gmA(map, node)
            for move in moves:
                if move not in visited:
                    queue.append(move)
                    pathFound[move] = node


def dfsr(map, start, goal, visited=[], path=[], depth=0, infiniteLoop=False):
    print()
    print("Depth is ", depth)
    depth += 1
    if depth > 90:
        print("Depth limit reached")
        return visited, False
    visited.append(start)
    printMap(map, start, goal)
    if start == goal:
        print("Goal found")
        path = [goal]
        return visited, True
    else:
        if infiniteLoop == False:
            moves = gmA(map, start)
        else:
            moves = gmB(map, start)
        for move in moves:
            print("Moves are ", moves)
            if True or move not in visited:
                if visited[len(visited)-2] == move:
                    print("Already visited (Parent)", move)
                    continue
                print("Visiting ", move)
                vis, fnd = dfsr(map, move, goal, visited,
                                path, depth+1, infiniteLoop)
                if fnd:
                    path.append(move)
                    return vis, fnd
                if visited[-1] == goal:
                    path = [goal]
                    return visited, True
    return visited, False


def createNewMap():

    map = []
    print("Enter the map rows: ")
    rows = int(input())
    print("Enter the map columns: ")
    cols = int(input())
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        map.append(row)
    print("Enter the map: \n 1 = wall \n 0 = path")
    for i in range(rows):
        for j in range(cols):
            text = "Enter the value for map[" + str(i) + "][" + str(j) + "] : "
            map[i][j] = int(input(text))
    return map
