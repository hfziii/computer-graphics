from vpython import *

windows = canvas(
    height = 1080,
    width = 600,
    background = color.black
)

cute = box(
    pos = vec(0,0,0),
    size = vec(1,1,1),
    axis = vec(0,0,0),
    color = color.green,
    canvas = windows
)