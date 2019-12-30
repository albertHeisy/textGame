# Any class that inherits from Weapon will automatically get the same behavior of the Weapon class for free
class Weapon:
    # namjerno stvaranje exceptionsa da se podsjetimo na neke stvari 
    # Za lakse debuganje kassnije ako napravimo gresku
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapon objects.')

    def __str__(self):
        return self.name    

class Rock(Weapon):
	def __init__(self):
		self.name = 'Rock'
		self.description = 'A fist-sized rock, suitable for bludgeoning.'
		self.damage = 5

class Dagger(Weapon):
	def __init__(self):
		self.name = 'Dagger'
		self.description = 'A small dagger with some rust.'\
							'Somewhat more dangerous than a rock.'
		self.damage = 10

class RustySword(Weapon):
	def __init__(self):
		self.name = 'Rusty Sword'
		self.description = 'This sword is showing its age, '\
							'but still has some fight in it.'
		self.damage = 20

class Axe(Weapon):
    def __init__(self):
        self.name = 'Axe'
        self.description = 'Design for cutting wood, '\
                                                        'maby can chop off parts of boy.'


