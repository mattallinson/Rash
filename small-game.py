class territory():

	def __init__(self, name, neighbours, owner, armies): # Countries have a name, neighbours, owners and armies
		self.name = name
		self.neighbours = neighbours
		self.owner = owner
		self.armies = armies

	def getName(self):
		return self.name

	def getNeighbours(self):
		return self.neighbours

	def getOwner(self):
		return self.owner

def makeCountries(country_name, neighbours):
	country = territory(str(country_name),neighbours, None, 1)

	return (country)

# Makes countries
	# two contries initally called East & West

map = {
	'East':['West'],
	'West':['East'],
}

# Make 2 Players

# assign the players random countries
	# add the first army to each territory

# let the players add their remaining 3 armies

# LET THE BATTLE COMMENCE

# If either player has more than one country

	# Player 1 goes first

		# Player 1 choses which country to attack 

		# Uses Risk_Roller to calculate the result

		# Changes the number of armies in the respective territories

	# Player 2 goes second

		# Repeats steps above

# Else (one player has lost all her countries)
	
	#Game Over, player who has won wins!
