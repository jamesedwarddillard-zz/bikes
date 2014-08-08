from bike_classes import *

#creating the world of wheels available
small_wheel = Wheels('small', 10)
medium_wheel = Wheels('medium', 15)
large_wheel = Wheels('large_wheel', 17)

#creating the world of frames available
aluminum = Frames('aluminum', 20, 0.5)
steel = Frames('steel', 7, 3.0)
carbon = Frames('carbon', 30, 0.7)

#creating bicycle models
light = Models('light', small_wheel, aluminum)
composite = Models('composite', medium_wheel, carbon)
rough = Models('rough', large_wheel, steel)

print light.weight
print composite.cost
print rough.maker
print light.name