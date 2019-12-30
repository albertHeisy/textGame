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

# vraca najjace oruzje u inventoriju
def most_powerfull_weapon(inventory):   
    max_damage = 0
    best_weapon = None
    for item in inventory:
        # ovaj exception handlig je zato kaj u inv nisu sve klase 
        # pa tako nemaju svi .damage
        try:
            if item.damage > max_damage:
                best_weapon = item.name
                max_damage = item.damage
        except AttributeError: # ovaj error se pojavi kad nisu svi kalse    
            pass
    return best_weapon 

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
        elif action_input == 'best':
            print(most_powerfull_weapon(inventory))
        else:
            print("Invalid action!")


play()
