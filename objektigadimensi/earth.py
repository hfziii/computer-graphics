from vpython import *

windows = canvas(
    height = 1080,
    width = 600,
    background = color.black
)

cute = sphere(
    pos = vec(0,0,0),
    radius = 1,
    axis = vec(1,1,1),
    texture = textures.earth,
    canvas = windows
)