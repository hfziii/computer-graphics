from vpython import *

scene = canvas(
    title = 'compound Object: Palu',
    width=800, height=600,
    background=color.black
)

handle = cylinder(
    size=vec(1,0.2,0.2),
    color=vec(0.72, 0.42, 0)
)

head = box(
    size=vec(0.2, 0.6, 0.2),
    pos=vec(1.1, 0, 0),
    color=color.gray(0.6)
)

hammer = compound ([handle, head])
hammer.axis = vec(1,1,0)