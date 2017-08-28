#!/usr/bin/python3

'''
Risk roller is a calculator for working out who wins a round in a game of risk
'''
import random

def dice_roll(number_of_dice): #returns a list of randomly generated numbers between 1 and 6, for a specified number of dice, sorted highest to lowest
	result = []
	for n in range(number_of_dice):
		result.append(random.randint(1,6))

	result.sort(reverse = True)

	return (result)

#get initial number of armies

attacker = int(input('Number of attacking armies:'))
defender = int(input('Number of defending armies:'))

# While Loop
game_round = 1
while attacker > 3 and defender > 0:
	# rolls 3 dice for attacker
	attacker_dice = dice_roll(3)

	# rolls 2 dice if attacker has >2 armies
	if defender >= 2:
		defender_dice = dice_roll(2)	
	# else rolls 1 die
	else :
		defender_dice = dice_roll(1)

	print('ROUND:', game_round, 'Attacker has', attacker, 'armies. Defenders has', defender,'armies.')
	print("Attacker Dice = ", attacker_dice)	
	print("Defender Dice = ", defender_dice)

	# calculates who wins for each roll
	defender_lose = 0
	attack_lose = 0
	for i in range(len(defender_dice)):		
		if attacker_dice[i] > defender_dice[i]:
			#attacker wins
			defender_lose += 1
			defender -= 1
		else:
			#defender wins
			attack_lose += 1
			attacker -= 1
	print('Defender loses: ', defender_lose , ' Attacker loses: ', attack_lose)
	game_round += 1
 
#If defender = 0 or attacker = 3, outputs the response
print('\n#####################\nAfter:',game_round,'rounds.') #LINE BREAK

if attacker <= 3:
	print('DEFENDER WINS. Attacker has', attacker, 'armies remaining. Defender has', defender,'armies remaining.' )

elif defender == 0:
	print('ATTACKER WINS: Attacker has', attacker, 'armies remaining' )
else:
	print('something\'s gone wrong')
print('#####################')