import pyglet


line_size = 40
window = pyglet.window.Window(280, 280)


@window.event
def on_draw():
    for ind, val in enumerate(make_empty_ms_grid(10)):
        pyglet.text.Label(val, 
        x=window.height//2, y=(ind + 0.5)*line_size,
        anchor_x="center", anchor_y="center").draw()

def make_empty_ms_grid(n):
    grid_draw = []
    for x in range(n):
        grid_draw.append(" ◻️ " * n)
        print(grid_draw)
    return grid_draw

pyglet.app.run()
