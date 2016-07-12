# Creates a new Class "Bike"
class Bike(object):
	# When instance of Bike Class (object) is created, user will input price and max_speed
	# the first paramater of ALL methods is the instance that method is being called on
	def __init__(self, price, max_speed):
		# this sets the price of that particular "Bike" as whatever user input
		self.price = price
		# this sets the max speed of that particular "Bike" as whatever user input
		self.max_speed = max_speed
		# this sets the miles upon creation of that particular "Bike" at 0
		self.miles = 0

	# function to show info, takes no parameters
	# the first parameter of ALL methods is the instance (self) that method is being called on
	# BUT you do not need to pass this as parameter (self) whenever invoked
	def displayInfo(self):
		# sets user input 'price' as string
		print "Price of this bike is:" + str(self.price)
		print "Max Speed of this bike is:" + str(self.max_speed)
		print "Miles Ridden is:" + str(self.miles)

	# function to add 10 miles, takes no parameters
	def ride(self):
		self.miles += 10
		print "Now riding..."
		# allows chaining
		return self 

	# function to subtract 5 miles, takes no parameters
	def reverse(self):
		# check to prevent negative miles
		if self.miles < 6:
			self.miles = 0
		else:
			self.miles -= 5
		print "Now reversing..."
		#allows chaining
		return self


#create 3 new instances of "Bike" class
bike1 = Bike('200', '25')
bike2 = Bike('500', '50')
bike3 = Bike('100', '12')


bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



