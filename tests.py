while True:
	try:
		num_armies = int(input('How many armies would you like to reinforce by?'))
		break
	except ValueError:
		print('please enter an integer number')

print('you would like to reinforce by', num_armies,'armies')