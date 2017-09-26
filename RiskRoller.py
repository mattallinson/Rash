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

def attack(attacker_armies, defender_armies,attack_stop,attacker_number_of_dice):
	attack_round = 1


	while attacker_armies > attack_stop and defender_armies > 0:
		# rolls  dice for attacker
		if attacker_armies >= 3:
			attacker_dice = dice_roll(3)
		elif attacker_armies == 2 or attacker_number_of_dice == 2:
			attacker_dice = dice_roll(2)
		elif attacker_armies == 1 or attacker_number_of_dice == 1:
			attacker_dice = dice_roll(1)

		# rolls 2 dice if attacker has >2 armies
		if defender_armies >= 2:
			defender_dice = dice_roll(2)	
		# else rolls 1 die
		else :
			defender_dice = dice_roll(1)

		print('ROUND:', attack_round, 'Attacker has', attacker_armies, 'armies. Defenders has', defender_armies,'armies.')
		print("Attacker Dice = ", attacker_dice)	
		print("Defender Dice = ", defender_dice)

		# calculates who wins for each roll
		defender_lose = 0
		attack_lose = 0
		for i in range(len(defender_dice)):		
			if attacker_dice[i] > defender_dice[i]:
				#attacker wins
				defender_lose += 1
				defender_armies -= 1
			else:
				#defender wins
				attack_lose += 1
				attacker_armies -= 1
		print('Defender loses: ', defender_lose , ' Attacker loses: ', attack_lose)
		attack_round += 1

	return{'round':attack_round, 'attacker_armies':attacker_armies, 'defender_armies': defender_armies}



def main():	
	#get initial number of armies
	attacker = int(input('Number of attacking armies:'))
	defender = int(input('Number of defending armies:'))

	attack_result = attack(attacker, defender,3,3)

	print('\n#####################\nAfter:',attack_result['round'],'rounds.') #LINE BREAK
	
	if attack_result['attacker_armies'] <=3 :
		print('DEFENDER WINS. Attacker has', attack_result['attacker_armies'], 'armies remaining. Defender has', attack_result['defender_armies'],'armies remaining.' )

	elif attack_result['defender_armies'] == 0:
		print('ATTACKER WINS: Attacker has', attack_result['attacker_armies'], 'armies remaining' )
	else:
		print('something\'s gone wrong, play Settlers of Catan instead.')
	print('#####################')

if __name__ == '__main__':
	main()