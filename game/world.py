class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError('Create a subclass instead!')

class StartTile(MapTile):
    def intro_text(self):
        return '''
        You find yourself in a cave with a flickering torch
        on the wall.
        You can make out four paths, each equally as dark
        and foreboding.
        '''
    def vicrory(self):
        return False

class BoringTile(MapTile):
    def intro_text(self):
        return '''
        This is a very boring part of the cave.
        '''
    def vicrory(self):
        return False

class VictoryTile(MapTile):
    def intro_text(self):
        return '''
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        
        Victory is yours !
        '''
    def vicrory(self):
        return True


def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
'''
 Grid of MAP 

 |0|1|2|
0 N V N
1 N B N
2 B S B
3 N B N
'''
world_map = [
[None, VictoryTile(1,0),None],
[None, BoringTile(1, 1),None],
[BoringTile(0,2), StartTile(1,2), BoringTile(2,2)],
[None,BoringTile(1,3),None]
]
