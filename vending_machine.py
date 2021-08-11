class vending_machine:
	### Try to find a 'major' deficit of this code ###
	def __init__(self):
		self.drink = []
		self.amount = []
		self.price = []

	def __str__(self):
		string = 'This machine have'
		for i, j in zip(self.drink, self.amount):
			append_string = '\n' + str(j) + str(': ') + str(i)
			string += append_string
		return string

	def putting_drink_in(self, drink_name, num_of_drink):
		""" For 1 kind of drink """
		""" different code according the drink is already in self.drink or not"""
		if drink_name in self.drink:
			drink_index = self.drink.index(drink_name)
			self.amount[drink_index] += num_of_drink
		else:
			self.drink.append(drink_name)
			self.amount.append(num_of_drink)
			self.price.append(0) # set price to 0

	def set_price(self, drink_name, price):
		if drink_name not in self.drink:
			print(f'please put your drink {drink_name} in vending machine first.')
		else:
			drink_index = self.drink.index(drink_name)
			self.price[drink_index] = price

	def remove_one_drink(self, drink_name):
		""" Remember you cannot buy multiple drinks at once in the vending machine  """
		if drink_name not in self.drink:
			print(f"We don't have such {drink_name}.")
		else:
			drink_index = self.drink.index(drink_name)
			if self.amount[drink_index] == 0:
				print(f'We are sorry. Your drink {drink_name} is sold out')
			else:
				self.amount[drink_index] -= 1
				return self.price[drink_index]

	def buy_a_drink(self, drink_name, input_money):
		""" A person gave some money and the drink name he wants to buy. We should give him a change """
		price = self.remove_one_drink(drink_name)
		if price == None: # which means we don't have such drink
			return input_money
		else:
			change = abs(input_money - price)
			print(f"here's your change {change} won.")
			print(f"have fun with your drink")
			return change


if __name__ == '__main__':
	vending_machine_1 = vending_machine()
	vending_machine_1.putting_drink_in('Coke', 30)
	vending_machine_1.set_price('Coke', 800)
	vending_machine_1.putting_drink_in('cider', 20)
	vending_machine_1.set_price('cider', 900)
	print(vending_machine_1)
	vending_machine_1.putting_drink_in('lemonade', 10)
	vending_machine_1.set_price('lemonade', 1200)
	print(vending_machine_1)
	vending_machine_1.putting_drink_in('Coke', 5)
	print(vending_machine_1)
	vending_machine_1.set_price('Zero Coke', 1200)
	vending_machine_1.buy_a_drink('Coke', 1000)
	print(vending_machine_1)