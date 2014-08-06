"""Creating a set of classes to model the bicycle industry, including:
Wheels
Frames
Models
Manufacturers
Shops
Customers"""

#defining the wheels class
class Wheels(object):
	def __init__(self, model, cost):
		self.model = model
		self.cost = cost
		self.weight = 1.0 #weight in pounds for all wheels		

# creating three wheel instances
smallwheels = Wheels('smallwheels', 50)
mediumwheels = Wheels('mediumwheels', 100)
bigwheels = Wheels('bigwheels', 150)

#defining the frames class 
class Frames(object):
	def __init__(self, materials, cost, weight):
		self.materials = materials
		self.cost = cost
		self.weight = weight

#creating three frame instances
aluminum = Frames('aluminum', 50, 1.0)
carbon = Frames('carbon', 125, 0.5)
steel = Frames('steel', 40, 2.5)