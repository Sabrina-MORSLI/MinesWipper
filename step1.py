import pyglet
# You will write a function named make_empty_ms_grid that takes a size n as
# argument and returns an n * n grid.

# Each cell will be initialised to a dictionary where a key 'state' is set to
# 'hidden', and a key 'content' is set to None (we'll fill the grid with bombs
# later on).

def make_empty_ms_grid(size_n):
    grid = []
    dic = {"content": None, "state": "hidden"}
    for x in range(size_n):
        grid.append([])
        # grid[x].extend([dic for i in range(size_n)])
    return grid

# print(make_empty_ms_grid(3))

my_grid = print(make_empty_ms_grid(10))

line_size = 50
window = pyglet.window.Window(400, 10*line_size)


@window.event
def on_draw():
    for ind, val in enumerate(my_grid):
        pyglet.text.Label(val, 
        x = window.width/2, y = (10 - ind - 0.5) * line_size,
        anchor_x="center", anchor_y="center").draw()
pyglet.app.run()
