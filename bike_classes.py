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

