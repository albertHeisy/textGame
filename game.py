from player import Player
import world

def get_player_command():
    return input('Action: ')


def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)

        print(room.intro_text())

        if room.vicrory() == True:
            break

        action_input = get_player_command().lower()

        if action_input == 'n':
            player.move_north()
        elif action_input == 's':
            player.move_south()
        elif action_input == 'e':
            player.move_east()
        elif action_input == 'w':
            player.move_west()
        elif action_input == 'i':
            player.print_inventroy()
        elif action_input == 'q':
            print('You exied the game')
            break
        else:
            print("Invalid action!")



play()
