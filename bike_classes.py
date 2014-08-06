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

#defining bicycle models class
class Models(object):
	maker = str()
	wholesale = int()
	retail = int()
	def __init__(self, name, wheels, frame):
		self.name = name
		self.wheels = wheels
		self.frame = frame
		self.weight = (wheels.weight *2) + frame.weight
		self.cost = (wheels.cost *2) + frame.cost

#creating a wholesale price function
def wholesale(manufactured_cost, margin):
	return manufactured_cost * (1+margin)

#defining bicycle manufacturers class
class Maker(object):
	def __init__(self, name, profit_margin, catalog):
		self.name = name
		self.profit_margin = profit_margin
		self.catalog = catalog
		for model in catalog: 
			model.wholesale = wholesale(model.cost, profit_margin)
			model.maker = self.name

#defining bike shops class
class Bike_shops(object):
	def __init__ (self, name, margin, inventory):
		self.name = name
		self.margin = margin
		self.inventory = inventory


	#print profit function

#creating bike purchase function
def bike_purchase(model, number, inventory):
	while True:
		try:
			inventory[model.name] += number
			return inventory
			break
		except KeyError:
			inventory[model.name] = number
			return inventory
			break


#defining customers class
class Customer(object):
	bikes = 0
	def __init__ (self, name, funds):
		self.name = name
		self.funds = funds
	#bike buying function


