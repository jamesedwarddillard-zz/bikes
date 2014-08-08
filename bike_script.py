from bike_classes import *

#creating the world of wheels available
small_wheel = Wheels('small', 10)
medium_wheel = Wheels('medium', 20)
large_wheel = Wheels('large_wheel', 30)

#creating the world of frames available
aluminum = Frames('aluminum', 40, 0.5)
steel = Frames('steel', 20, 3.0)
carbon = Frames('carbon', 100, 0.7)

#creating bicycle models 
super_light = Models('super light', small_wheel, aluminum)
light = Models('light', small_wheel, carbon)
composite = Models('composite', medium_wheel, carbon)
cheapo = Models('cheapo', small_wheel, steel)
rough = Models('rough', large_wheel, steel)
top_line = Models("top line", large_wheel, carbon)

#creating bike catalogs
minion_catalog = [light, composite, top_line]
pig_catalog = [cheapo, super_light, rough]

#creating bike makers
minion_bike_co = Maker('Minion Bike Co.', 0.0, minion_catalog)
pig_bikes = Maker('Pig Bikes', 0.0, pig_catalog)

#creating shop inventories

bru_stock1 = [minion_catalog[0], 20]
bru_stock2 = [pig_catalog[1], 20]
bru_stock3 = [minion_catalog[2], 20]
bru_stock4 = [pig_catalog[0], 10]
bru_stock5 = [minion_catalog[1], 10]
bru_stock6 = [pig_catalog[2], 10]
bikes_r_us_inventory = [bru_stock1, bru_stock2, bru_stock3, bru_stock4, bru_stock5, bru_stock6]

#creating bike shops
bikes_r_us = Bike_shops('Bikes R Us', .20, bikes_r_us_inventory)

#creating customers
Joy = Customer('Joy', 200)
John = Customer('Johnny', 500)
Eliza = Customer('Eliza', 1000)
customers = [Joy, John, Eliza]

#printing name and weight of each bike carried by the shop
print "Bike weights:"
for bikes in bikes_r_us.inventory:
	print bikes[0].name + "weighs approximately " + str(bikes[0].weight) + " pounds"
print ""

#printing customer name and the bikes they can afford
for person in customers: 
	print person.name + " cound purchase:"
	budget = person.funds
	for bikes in bikes_r_us.inventory:
		if budget > bikes[0].retail:
			print bikes[0].name + " costs " + str(bikes[0].retail)
	print ""

#printing bike inventory list
print "Bike availability"
for bikes in bikes_r_us.inventory:
	print bikes[0].name + ": " + str(bikes[1]) + " remaining"
print ""

#purchasing bikes
bike_purchase(4, bikes_r_us, Joy)
bike_purchase(6, bikes_r_us, John)
bike_purchase(3, bikes_r_us, Eliza)

#describing the purchases
for person in customers:
	print person.name + " bought " + person.bikes[-1].name + "for $" + str(person.bikes[-1].retail)
	print person.name + " has $" + str(person.funds) + " remaining in their bicycle fund."
	print ""

#printing store inventory remaining and profit
print "Bike availability"
for bikes in bikes_r_us.inventory:
	print bikes[0].name + ": " + str(bikes[1]) + " remaining"
print ""

#profit report
bikes_r_us.profit_report()


print ""
print 'revenue'
print bikes_r_us.revenue
print ""
print bikes_r_us.cogs
print "calculated profit"
profit = bikes_r_us.revenue - bikes_r_us.cogs
print profit
print ""
print profit / bikes_r_us.revenue

print bikes_r_us_inventory[3][0].retail + bikes_r_us_inventory[5][0].retail + bikes_r_us_inventory[2][0].retail
print bikes_r_us_inventory[3][0].wholesale + bikes_r_us_inventory[5][0].wholesale + bikes_r_us_inventory[2][0].wholesale
