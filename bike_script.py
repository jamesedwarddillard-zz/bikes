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
be_stock_1 = [pig_catalog[0], 10]
be_stock_2 = [minion_catalog[1], 10]
be_stock_3 = [pig_catalog[2], 10]
bike_emporium_inventory = [be_stock_1, be_stock_2, be_stock_3]

bru_stock1 = [minion_catalog[0], 20]
bru_stock2 = [pig_catalog[1], 20]
bru_stock3 = [minion_catalog[2], 20]
bikes_r_us_inventory = [bru_stock1, bru_stock2, bru_stock3]

#creating bike shops
bike_emporium = Bike_shops('Bike Emporium', .15, bike_emporium_inventory)
bikes_r_us = Bike_shops('Bikes R Us', .10, bikes_r_us_inventory)

#creating customers
Joy = Customer('Joy', 2000)
John = Customer('Johnny', 2500)
Eliza = Customer('Eliza', 10000)

bike_purchase(1, bikes_r_us, Joy)
print bikes_r_us.revenue
print bikes_r_us.cogs
bike_purchase(3, bikes_r_us, Joy)
print bikes_r_us.revenue
print bikes_r_us.cogs
