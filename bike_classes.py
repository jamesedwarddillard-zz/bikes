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
	def __init__(self, name, wheels, frame):
		self.name = name
		self.wheels = wheels
		self.frame = frame
		self.weight = (wheels.weight *2) + frame.weight
		self.cost = (wheels.cost *2) + frame.cost
		self.maker = str()
		self.wholesale = int()
		self.retail = int()

#creating a mark up price function
def markup(cost, margin):
	return cost * (1+margin)

#defining bicycle manufacturers class
class Maker(object):
	def __init__(self, name, profit_margin, catalog):
		self.name = name
		self.profit_margin = profit_margin
		self.catalog = catalog
		for model in catalog: 
			model.name = model.name + " by " + self.name
			model.wholesale = markup(model.cost, self.profit_margin)
			model.maker = self.name

#defining bike shops class
class Bike_shops(object):
	def __init__ (self, name, margin, inventory):
		self.name = name
		self.margin = margin
		self.inventory = inventory
		self.revenue = int()
		self.cogs = int()
		for item in inventory:
			item[0].retail = markup(item[0].wholesale, self.margin)
	def profit_report(self):
		profit = self.revenue - self.cogs
		print self.name + "has made $" + str(profit) + " in profit to date"



#creating bike purchase function
def bike_purchase(item_number, shop, customer):
	item_number -= 1
	#transfers $ from the customer
	customer.funds -= shop.inventory[item_number][0].retail
	#transfers $ to the shop
	shop.revenue += shop.inventory[item_number][0].retail
	shop.cogs += shop.inventory[item_number][0].wholesale
	
	#transfers ownership of bike to the customer
	customer.bikes.append(shop.inventory[item_number][0])
	#reduces bike from the shops inventory
	shop.inventory[item_number][1] -= 1


#defining customers class
class Customer(object):
	def __init__ (self, name, funds):
		self.name = name
		self.funds = funds
		self.bikes = []
	#bike buying function


