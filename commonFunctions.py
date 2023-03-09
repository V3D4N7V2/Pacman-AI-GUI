# Group 2
# Members:
#  BT19CSE004 Vedant Ghuge
#  BT19CSE082 Yashpal Singh Baghel
#  BT19CSE108 Dushyant Singh
#  BT19ECE036 Vishal Karangale

from pprint import pprint


def printMap(map, pacman, goal):
    print()
    for row in range(len(map)):
        for col in range(len(map[0])):
            if (row, col) == pacman:
                print('P ', end='')
            elif (row, col) == goal:
                print('G ', end='')
            else:
                if map[row][col] == 1:
                    print('# ', end='')
                else:
                    print('  ', end='')

        print()


def printMapPath(map, pacman, goal, path):
    print()
    for row in range(len(map)):
        for col in range(len(map[0])):
            if (row, col) == pacman:
                print('P ', end='')
            elif (row, col) == goal:
                print('G ', end='')
            else:
                if map[row][col] == 1:
                    print('# ', end='')
                else:
                    if (row, col) in path:
                        print('o ', end='')
                    else:
                        print('  ', end='')

        print()
