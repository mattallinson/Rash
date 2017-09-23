import random
import os
from terminaltables import AsciiTable

class territory():

	def __init__(self, name, neighbours, owner, armies): # Countries have a name, neighbours, owners and armies
		self.name = name
		self.neighbours = neighbours
		self.owner = owner
		self.armies = armies

	def output(self):
		return ("%s  \n%s : %s armies" %(self.name, self.owner, self.armies))


def makeCountries(country_name, neighbours):
	country = territory(str(country_name),neighbours, None, 1)

	return (country)

def countrySelector(player):
	random_country = random.choice(available_countries)
	available_countries.remove(random_country)
	countries_data[random_country].owner = player

def reinforce(player,max_armies):
	while max_armies >0:
		country_to_reinforce = input(player + ', which country would you like to reinforce? > ').title()
		if countries_data[country_to_reinforce].owner == player:
			break
		else:
			print('ERROR: You don\'t own a country with that name')
	if max_armies == 1:
		countries_data[country_to_reinforce].armies += 1
		max_armies -= 1
	else:
		armies_to_reinforce = int(input('How many armies would you like to reinforce with? > '))
		if armies_to_reinforce > max_armies:
			print('ERROR: you only have', max_armies, 'to reinforce with')
		else:
			countries_data[country_to_reinforce].armies += armies_to_reinforce
			max_armies -= armies_to_reinforce
	print(player, 'reinforcement complete!')



def print_playing_board():

	table_data = [
	['map', ''],
	[countries_data['West'].output(),countries_data['East'].output()]
	]

	table = AsciiTable(table_data)

	print(table.table)


map = {
	'East':['West'],
	'West':['East']
}

countries_data = {}
for c in [makeCountries(key,value) for key, value in map.items()]:
	countries_data[str(c.name)] = c

countries = [c for c in countries_data.keys()]
available_countries = list(countries)

player_1 = input('Enter name for Player 1 > ')
player_2 = input('Enter name for Player 2 > ')
players = [player_1, player_2]

while len(available_countries) != 0: #cycles through the players, assigning them a random country (that already has one occupying army)
	for p in players:
		countrySelector(p)

print_playing_board()

for p in players:
	reinforce(p,3)

print_playing_board()

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
