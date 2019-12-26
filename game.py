# Any class that inherits from Weapon will automatically get the same behavior of the Weapon class for free
class Weapon:
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

def get_player_command():
    return input('Action: ')

def play():
    inventory  = [Dagger(), 'Gold(5)','Crusty Bread', 'Bottle of wine']
    print("Escape from Cave Terror!")
    while True:
        action_input = get_player_command().lower()
        if action_input == 'n':
            print("Go North!")
        elif action_input == 's':
            print("Go South!")
        elif action_input == 'e':
            print("Go East!")
        elif action_input == 'w':
            print("Go West!")
        elif action_input == 'i':
            print('Inventory:')
            for i, item in enumerate(inventory,1):
                print('{}.{}'.format(str(i),str(item)))
        elif action_input == 'q':
            print('You exied the game')
            break
        else:
            print("Invalid action!")


play()
