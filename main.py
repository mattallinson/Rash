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

def player_input_own_country(player):
	while True:
			player_input_country = input(player + ', What country would you like to reinforce? >').title()
			if player_input_country in countries and countries_data[player_input_country].owner == player:
				break
			else:
				print('ERROR: Please enter a country you own.')
	
	return (player_input_country)

def player_input_army_size(player,max_army_size, army_type):
	while True:
		try:
			player_input_army = int(input(player + ', Please enter size of ' + army_type + '. You have ' +str(max_army_size)' armies remaining > '))
			if player_input_army <= max_army_size and player_input_army > 0:
				break
			else:
				print('ERROR: Please enter an army bigger than 0 and smaller than or equal to ' + str(max_army_size))
		except:
			print('ERROR: Please enter an integer number')

	return (player_input_army)



def reinforce(player,max_armies):
	while max_armies > 0:

		country_to_reinforce = player_input_own_country(player)
		
		if max_armies == 1:
			armies_to_reinforce = 1
		else:
			armies_to_reinforce = player_input_army_size(player,max_armies,'reinforcements.')

		print('Reinforcing', countries_data[country_to_reinforce].name, 'with', armies_to_reinforce ,'armies.')
		countries_data[country_to_reinforce].armies += armies_to_reinforce
		max_armies -= armies_to_reinforce

	print('Reinforcement for', player, 'is complete.')

def print_playing_board():

	table_data = [
	['map', ''],
	[countries_data['West'].output(),countries_data['East'].output()]
	]

	table = AsciiTable(table_data)

	print(table.table)

def main():
	game_round = 1

	for p in players: # Player 1 goes first
	print('Round', game_round, '.', p ,'\'s turn to attack.')
		if game_round != 1: #Delete this for boards bigger than 2 countries
			reinforce(p,3)
			print_playing_board()

		# Player 1 choses which country to attack 

		# Uses Risk_Roller to calculate the result

		# Changes the number of armies in the respective territories

		# Player 2 goes second

			# Repeats steps above

	# Else (one player has lost all her countries)
		
		#Game Over, player who has won wins!




#INITIALISES MAP
map = {
	'East':['West'],
	'West':['East']
}

countries_data = {} # returns a dictionary in the form {Country: <territoryObject>}
for c in [makeCountries(key,value) for key, value in map.items()]:
	countries_data[str(c.name)] = c

countries = [c for c in countries_data.keys()]
available_countries = list(countries)

#INITIALISES PLAYERS

player_1 = input('Enter name for Player 1 > ').title()
player_2 = input('Enter name for Player 2 > ').title()
players = [player_1, player_2]

#INITIALISES STARTING POSITIONS
while len(available_countries) != 0: #cycles through the players, assigning them a random country (that already has one occupying army)
	for p in players:
		countrySelector(p)

print_playing_board()

#OPENING REINFORCEMENT
for p in players:  
	reinforce(p,3)

print_playing_board()

# LET THE BATTLE COMMENCE
if __name__ == '__main__':
main()