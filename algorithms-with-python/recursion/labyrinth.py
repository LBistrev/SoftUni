"""
    You are given a labyrinth. Your goal is to find all paths from
    the start (cell 0, 0) to the exit, marked with 'e'.
-	Empty cells are marked with a dash '-'.
-	Walls are marked with a star '*'.
-   We can move in all 4 directions (up, down, left, right)
"""


def is_inbound(lab, row, col):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True
    return False


def is_exit(lab, row, col):
    if lab[row][col] == EXIT:
        global is_free
        is_free = True
        return True


WALL = '*'
TRACE = 'v'
EXIT = 'e'
EMPTY_CELL = '-'

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
is_free = False


def find_all_paths(row, col, labyrinth, direction, path):
    if is_inbound(labyrinth, row, col):
        return

    if labyrinth[row][col] == WALL:
        return

    if labyrinth[row][col] == TRACE:
        return

    path.append(direction)

    if is_exit(labyrinth, row, col):
        print(''.join(path))

    else:
        labyrinth[row][col] = TRACE

        find_all_paths(row, col + 1, labyrinth, RIGHT, path)
        find_all_paths(row, col - 1, labyrinth, LEFT, path)
        find_all_paths(row + 1, col, labyrinth, DOWN, path)
        find_all_paths(row - 1, col, labyrinth, UP, path)
        labyrinth[row][col] = EMPTY_CELL

    path.pop()


rows = int(input())
cols = int(input())
labyrinth = []

for _ in range(rows):
    labyrinth.append(list(input()))

find_all_paths(0, 0, labyrinth, '', [])

if not is_free:
    print(f'There is no way out!')
