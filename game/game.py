from player import Player

def get_player_command():
    return input('Action: ')


def play():
    print("Escape from Cave Terror!")
    player = Player()
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
            player.print_inventroy()
        elif action_input == 'q':
            print('You exied the game')
            break
        else:
            print("Invalid action!")


play()
