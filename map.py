'''
Country Name : {'Continent': answer, 'Occupier': None, 'Armies': None}
'''
map = {
	'Venezuela':{'Continent': 'South America','Occupier': None, 'Armies': None, 'Neighbours':['Brazil','Peru']},
	'Brazil':{'Continent': 'South America', 'Occupier': None, 'Armies': None, 'Neighbours':['Venezuela','Peru','Argentina','North Africa']},
	'Peru':{'Continent': 'South America', 'Occupier': None, 'Armies': None, 'Neighbours':['Venezuela','Brazil','Argentina']},
	'Argentina':{'Continent': 'South America', 'Occupier': None, 'Armies': None,'Neighbours':['Brazil','Peru'] }, 
	'North Africa':{'Continent': 'Africa', 'Occupier': None, 'Armies': None, 'Neighbours':['Brazil','Egypt','East Africa','Congo']},
	'Egypt':{'Continent': 'Africa', 'Occupier': None, 'Armies': None, 'Neighbours':['North Africa','East Africa']},
	'East Africa':{'Continent': 'Africa', 'Occupier': None, 'Armies': None, 'Neighbours':['Egypt','North Africa','Congo','South Africa']},
	'Congo':{'Continent': 'Africa', 'Occupier': None, 'Armies': None, 'Neighbours':['North Africa','East Africa','South Africa']},
	'South Africa':{'Continent': 'Africa', 'Occupier': None, 'Armies': None, 'Neighbours':['Congo','East Africa']}
	}
