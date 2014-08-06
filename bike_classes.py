"""Creating a set of classes to model the bicycle industry, including:
Wheels
Frames
Models
Manufacturers
Shops
Customers"""

"""classes go here"""

#defining the wheels class
class Wheels(object):
	def __init__(self, model, cost):
		self.model = model
		self.cost = cost
		self.weight = 1.0 #weight in pounds for all wheels		

#defining the frames class 
class Frames(object):
	def __init__(self, materials, cost, weight):
		self.materials = materials
		self.cost = cost
		self.weight = weight

#defining bicycle models
class Models(object):
	def __init__(self, name, wheels, frame, manufactuer):
		self.name = name
		self.wheels = wheels
		self.frame = frame
		self.manufactuer = manufactuer
		self.weight = (wheels.weight *2) + frame.weight
		self.cost = (wheels.cost *2) + frame.cost

"""instances go here"""

# creating three wheel instances
smallwheel = Wheels('smallwheels', 50)
mediumwheel = Wheels('mediumwheels', 100)
bigwheel = Wheels('bigwheels', 150)

#creating three frame instances
aluminum = Frames('aluminum', 50, 1.0)
carbon = Frames('carbon', 125, 0.5)
steel = Frames('steel', 40, 2.5)