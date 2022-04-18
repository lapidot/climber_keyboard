import cadquery as cq

height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0

# make the base
# result = cq.Workplane("XY").box(height, width, thickness)\
#     .faces(">Z").workplane().hole(diameter)\
#     .faces(">Z").workplane() \
#     .rect(height - padding, width - padding, forConstruction=True)\
#     .vertices()\
#     .cboreHole(2.4, 4.4, 2.1)\
#     .edges("|Z").fillet(2.0)

# result = cq.Workplane("XY")

result = (
   cq.Sketch()
   .trapezoid(4,3,90)
   .vertices()
   .circle(.5, mode='s')
   .reset()
   .vertices()
   .fillet(.25)
   .reset()
   .rarray(.6,1,5,1).slot(1.5,0.4, mode='s', angle=90)
)

# Render the solid
# show_object(result)
show(result)
