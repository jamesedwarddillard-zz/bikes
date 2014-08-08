from bike_classes import *

#creating the world of wheels available
small_wheel = Wheels('small', 10)
medium_wheel = Wheels('medium', 15)
large_wheel = Wheels('large_wheel', 30)

#creating the world of frames available
aluminum = Frames('aluminum', 40, 0.5)
steel = Frames('steel', 17, 3.0)
carbon = Frames('carbon', 90, 0.7)

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
minion_bike_co = Maker('Minion Bike Co.', 0.2, minion_catalog)
pig_bikes = Maker('Pig Bikes', 0.21, pig_catalog)

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
for bikes in bikes_r_us.inventory:
	print bikes[0].name + "weighs approximately " + str(bikes[0].weight) + " pounds"

#printing customer name and the bikes they can afford
for person in customers: 
	print person.name
	budget = person.funds
	for bikes in bikes_r_us.inventory:
		if budget > bikes[0].retail:
			print bikes[0].name + " costs " + str(bikes[0].retail)

