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
	def __init__(self, cost, materials):
		self.cost = cost
		self.materials = materials
		weight = 2.0 #weight in pounds