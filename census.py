class Person:
	# __init__ -- potreban je za inicijalizaciju kalase 
	# svaki argument koji passamo unutra postaje obavezan za stvaranje objekta 
	# argument self stavljamo zato sto on referira na bas taj objekt tipa da age nije univerzalan
	# nego je vezan za tu osobu nad kojom je pozvan, koju stvara 
	def __init__(self, name, age, favourite_foods):
		self.age= age
		self.name = name 
		self.favourite_foods = favourite_foods 

	def __str__(self):
		return 'Name: {} Age: {} Favourite food: {}'.format(self.name, self.age, self.favourite_foods[0])
	# moramo passat self da mozemo doci do godina
	def birth_year(self):
		return 2015 - self.age

people = [Person('Ed', 11,['hotdogs', 'jawbreakers']), Person('Edd', 11, ['broccoli']), Person('Eddy', 12, ['chunky puffs',
'jawbreakers'])]

age_sum = 0
year_sum = 0

for person in people:
	age_sum += person.age
	year_sum += person.birth_year()

print('The average age is: ' + str(age_sum / len(people)))
print('The average birth year is: ' + str(int(year_sum / len(people))))

print('The people polled in this census were:')
for person in people:
	print(person)
