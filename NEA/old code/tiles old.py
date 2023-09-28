#MAP

import pygame,csv,os
#TileClass
class Tile(pygame.sprite.Sprite):
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x, self.rect.y))
#TileMap
class TileMap():
    def __init__(self,filename):
        self.tile_size = 36
        self.start_x, self.start_y = 0,0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w,self.map_h))
        self.map_surface.set.colorkey((0,0,0))
        self.load_map()
    def draw_map(self, surface):
        surface.blit(self.map_surface,(0,0))
    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
    def read_csv(self,filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data,delimiter=",")
            for row in data:
                map.append(list(row))
        return map
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x,y = 0,0
        for row in map:
            x = 0
            for tile in row:
                if tile == '21':
                    tiles.append(Tile('tile_0021.png', x * self.tile_size, y * self.tile_size))
                elif tile == '22':
                    tiles.append(Tile('tile_0022.png', x * self.tile_size, y * self.tile_size))
                elif tile == '23':
                    tiles.append(Tile('tile_0023.png', x * self.tile_size, y * self.tile_size))
                elif tile == '121':
                    tiles.append(Tile('tile_0121.png', x * self.tile_size, y * self.tile_size))
                elif tile == '122':
                    tiles.append(Tile('tile_0122.png', x * self.tile_size, y * self.tile_size))
                elif tile == '123':
                    tiles.append(Tile('tile_0123.png', x * self.tile_size, y * self.tile_size))
                elif tile == '124':
                    tiles.append(Tile('tile_0124.png', x * self.tile_size, y * self.tile_size))
                elif tile == '125':
                    tiles.append(Tile('tile_0125.png', x * self.tile_size, y * self.tile_size))
                elif tile == '141':
                    tiles.append(Tile('tile_0141.png', x * self.tile_size, y * self.tile_size))
                elif tile == '142':
                    tiles.append(Tile('tile_0142.png', x * self.tile_size, y * self.tile_size))
                elif tile == '143':
                    tiles.append(Tile('tile_0143.png', x * self.tile_size, y * self.tile_size))
                print(tiles)
                x += 1
            y+=1