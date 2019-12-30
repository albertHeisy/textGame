import items 

class Player:
    def __init__(self):
        self.inventory = [items.Rock(), items.Dagger(), 'Gold(5)', 'Crusty Bread']
    
    def print_inventroy(self):
        print('Inventory: ')
        for i, item in enumerate(self.inventory):
            print('{}.{}'.format(str(i), str(item)))
        best_weapon = self.most_powerful_weapon()
        print('Your best wepon is {}.'.format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            # ovaj exception handlig je zato kaj u inv nisu sve klase 
            # pa tako nemaju svi .damage
            try:
                if item.damage > max_damage:
                    best_weapon = item.name
                    max_damage = item.damage
            except AttributeError: # ovaj error se pojavi kad nisu svi kalse    
                pass
        return best_weapon 


        

        
