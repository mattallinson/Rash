from map import map
from terminaltables import AsciiTable 
import random

countries = [c for c in map.keys()] #list the countries in the chosen map
available_countries = list(countries)

def country_selector(player):
	for i in range (3):
		random_country = random.choice(available_countries)
		available_countries.remove(random_country)
		player['countries'].setdefault(random_country,1)

def reinforce(player,num_armies):
	while True:						#finds out which country you want to reinforce
		country_to_reinforce = input(player['name'] + ', which country would you like to reinforce? > ').title()
		if country_to_reinforce in player['countries'].keys():
			break
		else:	#Handles typos etc
			print('ERROR: You don\'t own a country with that name')
	if num_armies == None: 
		while True:
			try:
				num_armies = int(input('How many armies would you like to reinforce by?> '))
				break
			except ValueError:
				print('ERROR: please enter an integer number')
			
	player['countries'][country_to_reinforce] += num_armies

	armies_used =int(num_armies)
	return (armies_used)


# Set up three players, give them names and a list of contries they hold, 
# player_X = {'Name':'name of player',countries:{country one:number of armies in country one, country two: number of armies in country two,...}}
player_1 = {'name':None,'countries':{}}
player_2 = {'name':None,'countries':{}}
player_3 = {'name':'Computer','countries':{}}
players = [player_1, player_2, player_3]

player_1['name'] = input('Enter name for Player 1 > ')
player_2['name'] = input('Enter name for Player 2 > ')

for p in players: #Assign countries to player 
	country_selector(p)


table_data = [
	[player_1['name'],player_2['name'],player_3['name']],
	[[k for k in player_1['countries']][0],[k for k in player_2['countries']][0], [k for k in player_3['countries']][0]],
	[[k for k in player_1['countries']][1],[k for k in player_2['countries']][1], [k for k in player_3['countries']][1]],
	[[k for k in player_1['countries']][2],[k for k in player_2['countries']][2], [k for k in player_3['countries']][2]]
]

table = AsciiTable(table_data)
print (table.table)