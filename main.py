#!/usr/bin/python3

import random
import os
import math
from terminaltables import AsciiTable
import RiskRoller as rr 

class territory():

	def __init__(self, name, neighbours, owner, armies): # Countries have a name, neighbours, owners and armies
		self.name = name
		self.neighbours = neighbours
		self.owner = owner
		self.armies = armies

	def output(self):
		return ("%s  \n%s : %s armies" %(self.name, self.owner, self.armies))

class player():

	def __init__(self,name,country_count):
		self.name = name
		self.country_count = country_count


def makeCountries(country_name, neighbours):
	country = territory(str(country_name),neighbours, None, 1)

	return (country)

def countrySelector(player):
	random_country = random.choice(available_countries)
	available_countries.remove(random_country)
	countries_data[random_country].owner = player.name
	player.country_count += 1


def player_input_own_country(player):
	while True:
			player_input_country = input(player.name + ', What country would you like to reinforce? >').title()
			if player_input_country in countries and countries_data[player_input_country].owner == player.name:
				break
			else:
				print('ERROR: Please enter a country you own.')
	
	return (player_input_country)

def player_input_army_size(player,max_army_size, army_type):
	while True:
		try:
			player_input_army = int(input(str(player.name) + ', Please enter size of ' + army_type + ' You have ' +str(max_army_size) + ' armies remaining > '))
			if player_input_army <= max_army_size and player_input_army > 0:
				break
			else:
				print('ERROR: Please enter an army bigger than 0 and smaller than or equal to ' + str(max_army_size))
		except:
			print('ERROR: Please enter an integer number')

	return (player_input_army)



def reinforce(player):
	max_armies = math.floor(player.country_count/3)+3

	while max_armies > 0:

		country_to_reinforce = player_input_own_country(player)
		
		if max_armies == 1:
			armies_to_reinforce = 1
		else:
			armies_to_reinforce = player_input_army_size(player,max_armies,'reinforcements.')

		print('Reinforcing', countries_data[country_to_reinforce].name, 'with', armies_to_reinforce ,'armies.')
		countries_data[country_to_reinforce].armies += armies_to_reinforce
		max_armies -= armies_to_reinforce

	print('Reinforcement for', player.name, 'is complete.')

def print_playing_board(): #I would love for this to be able any size map

	table_data = [
	['map', ''],
	[countries_data['West'].output(),countries_data['East'].output()]
	]

	table = AsciiTable(table_data)

	print(table.table)

def player_input_enemy_country(attacking_country, player):
	while True:
		player_input_country = input(player.name + ', What country would you like to attack? >').title()
		if player_input_country in countries and countries_data[player_input_country].owner =! player.name and attacking_country in countries_data[player_input_country].neighbours:
				break
			else:
				print('ERROR: Please enter a valid country you can attack from', attacking_country)
	
	return (player_input_country)

def attack(player):
	
	attacking_from = player_input_own_country(player) #ask player which country they want to attack from
	defending_country = player_input_enemy_country(attacking_from, player) #asks player which country they would like to attack
	#asks player what point to stop the attack


	#asks player how many dice they would like to use

	#calls risk roller

def main():
	game_round = 1

	while player_1.country_count >0 or player_2.country_count > 0:
		for p in players: # Player 1 goes first
			print('Round', math.floor(game_round), '.', p.name + '\'s turn to attack.')
			
			if len(countries) == 2:
				if math.floor(game_round) != 1:
						reinforce(p)
						print_playing_board()
			else:
				reinforce(p)
				print_playing_board()

			'''
			########################

			INSERT REST OF GAME HERE

			########################

			'''


			game_round +=0.5

	# Else (one player has lost all her countries)
		
		#Game Over, player [who has won] wins!

#INITIALISES MAP
map = {
	'East':['West'],
	'West':['East']
}

countries_data = {} # returns a dictionary in the form {Country: <territoryObject>}
for c in [makeCountries(country_name,neighbours) for country_name, neighbours in map.items()]:
	countries_data[str(c.name)] = c

countries = [c for c in countries_data.keys()]
available_countries = list(countries)

#INITIALISES PLAYERS

player_1 = player(input('Enter name for Player 1 > ').title(),0)
player_2 = player(input('Enter name for Player 2 > ').title(),0)
players = [player_1, player_2]

#INITIALISES STARTING POSITIONS
while len(available_countries) != 0: #cycles through the players, assigning them a random country (that already has one occupying army)
	for p in players:
		countrySelector(p)

print_playing_board()

#OPENING REINFORCEMENT
for p in players:  
	reinforce(p)

print_playing_board()

# LET THE BATTLE COMMENCE
if __name__ == '__main__':
	main()