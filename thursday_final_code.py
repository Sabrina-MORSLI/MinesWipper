import random


def make_empty_ms_grid(size_n):
    grid = []
    for _ in range(size_n):
        sub_list = []
        for _ in range(size_n):
            sub_list.append({'content': None, 'state': 'hidden'})
        grid.append(sub_list)
    return grid

def add_bombs(grid):
    number_bombs = len(grid)*len(grid)//3
    print(number_bombs)
    for i in range(1, number_bombs):
        x = random.randrange(len(grid))
        y = random.randrange(len(grid))
        grid[x][y]["content"] = "b"
    return grid
grid = make_empty_ms_grid(3)   # this is hard coded fix it
print(*add_bombs(grid), sep="\n")


def find_adjacent_mines(grid, x, y):
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
    print(*grid, sep="\n")


find_adjacent_mines(grid, 3, 3)



