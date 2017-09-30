#!/usr/bin/python3

import random
import os
import math
from terminaltables import AsciiTable
import RashRoller as rr 

class territory():

	def __init__(self, name, neighbours, owner, armies): # Countries have a name, neighbours, owners and armies
		
		self.name = name
		self.neighbours = neighbours
		self.owner = owner
		self.armies = armies

	def output(self):
		return ("%s  \n%s : %s armies" %(self.name, self.owner.name, self.armies))

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
	countries_data[random_country].owner = player
	player.country_count += 1

def player_input_own_country(player, message):
	while True:
			player_input_country = input(player.name + ', What country would you like to ' + message +'? >\t').title()
			if player_input_country in countries and countries_data[player_input_country].owner.name == player.name:
				break
			else:
				print('ERROR: Please enter a country you own.')
	
	return (player_input_country)

def player_input_number(player,max_number, min_number, message):	
	while True:
		try:
			player_input_number = int(input(str(player.name) + ', Please enter '  + message  + '. Maximum: ' +str(max_number) + '>\t'))
			if player_input_number <= max_number and player_input_number >= min_number:
				break
			else:
				print('ERROR: Please enter a number bigger than ' + str(min_number) + 'and smaller than or equal to ' + str(max_number))
		except:
			print('ERROR: Please enter an integer number')

	return (player_input_number)

def reinforce(player):
	#print_playing_board()
	max_armies = math.floor(player.country_count/3)+3

	while max_armies > 0:

		country_to_reinforce = player_input_own_country(player, 'reinforce')
		
		if max_armies == 1:
			armies_to_reinforce = 1
		else:
			armies_to_reinforce = player_input_number(player,max_armies,0,'size of reinforcements')

		print('Reinforcing', countries_data[country_to_reinforce].name, 'with', armies_to_reinforce ,'armies.')
		countries_data[country_to_reinforce].armies += armies_to_reinforce
		max_armies -= armies_to_reinforce

	print('Reinforcement for', player.name, 'is complete.\n')
	clearScreen()

def print_playing_board(): #I would love for this to be able any size game_map

	table_data = [
	['Map', ''],
	[countries_data['West'].output(),countries_data['East'].output()]
	]

	table = AsciiTable(table_data)

	print(table.table)

def player_input_enemy_country(attacking_country, player):
	while True:
		player_input_country = input(player.name + ', What country would you like to attack? >\t').title()
		if player_input_country in countries and countries_data[player_input_country].owner.name != player.name and attacking_country in countries_data[player_input_country].neighbours:
			break
		else:
			print('ERROR: Please enter a valid country you can attack from', attacking_country)
	
	return (player_input_country)

def max_dice(country):
	if country.armies > 3:
		max_dice = 3
	else:
		max_dice = country.armies -1 

	return max_dice

def attack(player):
	
	attacking_from = player_input_own_country(player,'attack from') # ask player which country they want to attack from
	defending_country = player_input_enemy_country(attacking_from, player) # asks player which country they would like to attack	
	number_of_dice = player_input_number(player,max_dice(countries_data[attacking_from]), 0, 'number of dice to attack with')# asks player how many dice they would like to use	
	stopping_point = player_input_number(player, int(countries_data[attacking_from].armies-number_of_dice), 0,'the number of armies you want remaining after the attack') # asks player what point to stop the attack	
	
	clearScreen()
	attack_result = rr.attack(countries_data[attacking_from].armies, countries_data[defending_country].armies,number_of_dice,stopping_point)  # calls risk roller

	if attack_result['defender_armies'] == 0: # if attacker wins
		print(player.name, 'wins with', attack_result['attacker_armies'], 'armies remaining' )
		countries_data[defending_country].owner.name = player.name
		player.country_count += 1
		countries_data[defending_country].owner.country_count -= 1
		if countries_data[defending_country].owner.country_count == 0:
			countries_data[defending_country].armies = 0
			return
		number_of_occupying_armies = player_input_number(player, attack_result['attacker_armies']-1, attack_result['attacker_dice_count'] ,'the number of armies you want to move')
		countries_data[defending_country].armies = number_of_occupying_armies
		countries_data[attacking_from].armies =  attack_result['attacker_armies'] - number_of_occupying_armies

		
	else: # if defender wins
		print('Attack stopped. ', player.name, 'has', attack_result['attacker_armies'], 'armies remaining. ', countries_data[defending_country].owner.name, 'has ', attack_result['defender_armies'], 'remaining.')
		countries_data[attacking_from].armies = attack_result['attacker_armies']
		countries_data[defending_country].armies = attack_result['defender_armies']	 

def player_input_y_or_n(player, message):
	while True:
		player_input = input(player.name + ', Would you like to ' + message + ', Y/N? > \t').lower().rstrip()
		if player_input == 'y' or player_input == 'n':
			break
		else:
			print('ERROR: Please enter either a y (for yes) or a n (for no)')
	
	return (player_input)

def player_countries(player):

	player_countries = []
	
	for c in country_list:
		if c.owner == player:
			player_countries.append(c)

	return player_countries

def player_can_attack(player):
	
	countries_can_attack = 0
	for pc in player_countries(player):
		if pc.armies > 1:
			countries_can_attack +=1

	if countries_can_attack > 0:
		attack_ready = True

	else: 
		attack_ready = False

	return attack_ready

def clearScreen():
	tmp = os.system('clear')

def pauseGame():

	tmp = input('\t Press \'Enter\' to continue:')

def main():

	clearScreen()
	print('Hello and welcome to', '\033[1m', '\033[91m', '\nRash: Version 1 \nThe Cold War: Abridged\n','\033[0m',)

	#INITIALISES l
	player_1 = player(input('Enter name for Player 1 > ').title(),0)
	player_2 = player(input('Enter name for Player 2 > ').title(),0)
	players = [player_1, player_2]

	clearScreen()


	#INITIALISES STARTING POSITIONS
	while len(available_countries) != 0: #cycles through the players, assigning them a random country (that already has one occupying army)
		for p in players:
			countrySelector(p)
		

	#OPENING REINFORCEMENT
	for p in players:  
		print_playing_board()
		reinforce(p)

	clearScreen()
	print_playing_board()


	round_count = 1

	while player_1.country_count >0 or player_2.country_count > 0:
		for p in players: # Player 1 goes first
			print('Round', math.floor(round_count), '.', p.name + '\'s turn to attack.')
			
			if len(countries) == 2:
				if math.floor(round_count) != 1:
						reinforce(p)
						print_playing_board()
			else:
				reinforce(p)
				print_playing_board()

			while True:
				if player_can_attack(p):
					attack_this_round = player_input_y_or_n(p,'attack a country')
					if attack_this_round == 'y':
						attack(p)
						#print_playing_board()
					else:
						break
					if player_1.country_count == 0 or player_2.country_count == 0:
						break
				else:
					break


			print('round for', p.name, 'complete.')
			if player_1.country_count == 0 or player_2.country_count == 0:
				break
			round_count +=0.5
			pauseGame()
			print_playing_board()
			clearScreen()
			print_playing_board()
	
		if player_1.country_count == 0:			
			print('After',str(math.floor(round_count)),'rounds.',player_2.name, 'wins!!!!\n!!!!!!!!!!!!!!!')
			print_playing_board()
			return

		elif player_2.country_count == 0:
			print('After',str(math.floor(round_count)),'rounds.',player_1.name, 'wins!!!!\n!!!!!!!!!!!!!!!')
			print_playing_board()
			return


#INITIALISES MAP
game_map = {
	'East':['West'],
	'West':['East']
}

country_list = [makeCountries(country_name,neighbours) for country_name, neighbours in game_map.items()]
countries_data = {} # returns a dictionary in the form {Country: <territoryObject>}
for c in country_list:
	countries_data[str(c.name)] = c

countries = [c for c in countries_data.keys()]
available_countries = list(countries)

# LET THE BATTLE COMMENCE
if __name__ == '__main__':
	main()
