def get_player_command():
    return input('Action: ')

def play():
    inventory  = ['Dagger', 'Gold(5)','Crusty Bread', 'Bottle of wine']
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
        else:
            print("Invalid action!")


play()