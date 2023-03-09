# Group 2
# Members:
#  BT19CSE004 Vedant Ghuge
#  BT19CSE082 Yashpal Singh Baghel
#  BT19CSE108 Dushyant Singh
#  BT19ECE036 Vishal Karangale



from commonFunctions import *
from pacman_ai_bfs import bfs

defaultMap = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

defaultStart = (6, 1)
defaultGoal = (3, 3)


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
            map[i][j] = int(input())
    return map


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


def dfs(map, start, goal):
    stack = []
    stack.append(start)
    visited = []
    visited.append(start)
    while stack:
        node = stack.pop()
        if node == goal:
            return visited
        else:

            moves = gmB(map, node)
            for move in moves:
                if move not in visited:
                    stack.append(move)
                    visited.append(move)


def dfsr(map, start, goal, visited=[], path=[]):
    print()
    visited.append(start)
    printMap(map, start, goal)
    if start == goal:
        print("Goal found")
        path = [goal]
        return visited, True
    else:
        moves = gmB(map, start)

        for move in moves:
            print("Moves are ", moves)
            if True or move not in visited:
                if visited[len(visited)-2] == move:
                    print("Already visited (Parent)", move)
                    continue
                print("Visiting ", move)
                vis, fnd = dfsr(map, move, goal, visited, path)
                if fnd:
                    path.append(move)
                    return vis, fnd
                if visited[-1] == goal:
                    path = [goal]
                    return visited, True
    return visited, False


def main():
    map = defaultMap
    print("Playing Game using DFS")
    print("Create a new map? (y/n)")
    if input() == "y":
        map = createNewMap()
        print("Created new map")

    else:
        print("Using default map")
    print("Map is : ")
    printMap(map, (-1, -1), (-1, -1))

    print("Change start and goal? (y/n)")
    if input() == "y":
        while True:
            print("Enter start coordinates: ")
            start = (int(input("Start Row : ")), int(input("Start Col : ")))
            print("Enter goal coordinates: ")
            goal = (int(input("Goal Row : ")), int(input("Goal Col : ")))
            if map[start[0]][start[1]] == 1 or map[goal[0]][goal[1]] == 1:
                print("Invalid coordinates")
            else:
                break
    else:
        start = defaultStart
        goal = defaultGoal

    print("Starting with Map: ")
    printMap(map, start, goal)

    if input("Run BFS (y/n)") == "y":
        print("Running BFS")
        print(bfs(map, start, goal))
    if input("Run DFS (y/n)") == "y":
        print("Running DFS")
        visited = []
        path = []
        vi, found = dfsr(map, start, goal, visited, path)
        print(vi)
        if found:
            path.append(start)
            path.reverse()
            print("Path is : ", path)
            printMapPath(map, -1, -1, path)


if __name__ == "__main__":
    main()
