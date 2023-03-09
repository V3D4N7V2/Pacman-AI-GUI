# Group 2
# Members:
#  BT19CSE004 Vedant Ghuge
#  BT19CSE082 Yashpal Singh Baghel
#  BT19CSE108 Dushyant Singh
#  BT19ECE036 Vishal Karangale

from commonFunctions import *

map = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]


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
            return visited
        else:

            moves = gmA(map, node)
            for move in moves:
                if move not in visited:
                    queue.append(move)
                    pathFound[move] = node


def main():
    print("Playing Game using BFS")

    print("Visited Nodes List ", bfs(map, (6, 1), (3, 3)))


if __name__ == "__main__":
    main()
