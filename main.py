from map import map
import random

countries = [c for c in map.keys()] #list the countries in the chosen map
available_countries = list(countries)

def country_selector(player):
	for i in range (3):
		random_country = random.choice(available_countries)
		available_countries.remove(random_country)
		player['Countries'].setdefault(random_country,1)


# Set up three players, give them names and a list of contries they hold, 
# player_X = {'Name':'name of player',Countries:{country one:number of armies in country one, country two: number of armies in country two,...}}
player_1 = {'Name':None,'Countries':{}}
player_2 = {'Name':None,'Countries':{}}
player_3 = {'Name':'Computer','Countries':{}}
players = [player_1, player_2, player_3]

for p in players: #Assign countries to player 
	country_selector(p)
