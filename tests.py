max_armies = 5
while max_armies > 0:
	armies_to_reinforce = int(input('How many armies would you like to reinforce with? > '))
	if armies_to_reinforce > max_armies:
		print('ERROR: you only have', max_armies, 'to reinforce with')
	else:
		max_armies -= armies_to_reinforce
	
print('reinforcement complete')
