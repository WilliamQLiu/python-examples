import pyglet
from pyglet.window import key
from pyglet.window import mouse


window = pyglet.window.Window()
label = pyglet.text.Label(
    'Hello world', x=window.width//2, y=window.height//2,
    anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    """ Detect Key Press """
    if symbol == key.A:
        print "The 'A' key was pressed."
    elif symbol == key.LEFT:
        print "The left arrow key was pressed."
    elif symbol == key.RIGHT:
        print "The right arrow key was pressed."
    elif symbol == key.ENTER:
        print "The enter key was pressed"


pyglet.app.run()
