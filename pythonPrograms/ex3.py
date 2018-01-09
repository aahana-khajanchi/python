cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car		#120
average_passengers_per_car = passengers / cars_driven	#3

print ("There are ", cars, "cars available.")
print ("There are only",(drivers),"drivers available")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport",carpool_capacity, "people today.")
print ("we have", passengers, "to carpool today")
print ("we need to put about", average_passengers_per_car, "in each car")




my_name = 'zed a sha.w'
my_age = 35 
my_height = 74
my_weight = 180

print ("let's talk {0} " .format(my_name))
print ("he's {0} inches." .format(my_height))
print ("height n weight" .format(my_height,my_weight))

print ("if i add {0} , {1} , and {2}  I get {3}." .format(my_age,my_height,my_weight, my_age + my_height + my_weight))


