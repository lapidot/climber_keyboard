import cadquery as cq

height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0

result = (
    cq.Sketch()
    .trapezoid(100, 80, 90, tag='base')
    .vertices()
    .fillet(2)
    .reset()
    .center(-50,0)
    .rarray(18, 17, 5, 1)
    .rarray(18, 17, 1, 3)
    .rect(14, 14, mode='s', tag='key')
    .reset()
)

# Render the solid
# show_object(result)
show(result)
