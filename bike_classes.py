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







"""instances go here"""

# creating three wheel instances
smallwheel = Wheels('smallwheels', 50)
mediumwheel = Wheels('mediumwheels', 100)
bigwheel = Wheels('bigwheels', 150)

#creating three frame instances
aluminum = Frames('aluminum', 50, 1.0)
carbon = Frames('carbon', 125, 0.5)
steel = Frames('steel', 40, 2.5)

# scratch for testing

big_bike = Models('bigassbike', bigwheel, steel)
light_bike = Models('airbike', smallwheel, carbon)
bike_list = [big_bike, light_bike]

james_bikes = Maker("James's Bike Co.", 0.40, bike_list)

for i in james_bikes.catalog:
	print i.name, i.wholesale, i.maker
