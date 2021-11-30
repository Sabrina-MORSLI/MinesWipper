import random

global x
global y
global grid


def add_bombs(x, y):
    grid = make_empty_ms_grid(x, y)
    number_bombs = x*y//3
    for i in range(number_bombs):
        x = random.randrange(len(grid))
        y = random.randrange(len(grid))
        grid[x][y]["content"] = "b"
    return grid


def make_empty_ms_grid(x, y):
    grid = []
    for _ in range(y):
        sub_list = []
        for _ in range(x):
            sub_list.append({'content': None, 'state': 'hidden'})
        grid.append(sub_list)
    return grid


def find_adjacent_mines(x, y):
    grid = add_bombs(x, y)
    for i in range(y):
        for j in range(x):
            if grid[i][j]["content"] is None:
                mine_count = 0
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        if 0 <= a < y and 0 <= b < x:
                            if grid[a][b]["content"] == "b":
                                mine_count = mine_count + 1
                grid[i][j]["content"] = mine_count
    return grid

print(*find_adjacent_mines(4, 3), sep="\n")


