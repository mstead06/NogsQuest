######################################Tiles 2.0######################################

import pygame

TILESIZE = 36
#load images (in order of when i added them so i dont have to change indexes everytime i use a new tile

tile_0021 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0021.png'), (36,36))
tile_0022 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0022.png'), (36,36))
tile_0023 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0023.png'), (36,36))
tile_0121 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0121.png'), (36,36))
tile_0122 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0122.png'), (36,36))
tile_0123 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0123.png'), (36,36))
tile_0124 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0124.png'), (36,36))
tile_0125 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0125.png'), (36,36))
tile_0141 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0141.png'), (36,36))
tile_0142 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0142.png'), (36,36))
tile_0143 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0143.png'), (36,36))
tile_0088 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0088.png'), (36,36))
tile_0001 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0001.png'), (36,36))
tile_0002 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0002.png'), (36,36))
tile_0003 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0003.png'), (36,36))
tile_0017 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0017.png'), (36,36))
tile_0018 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0018.png'), (36,36))
tile_0019 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0019.png'), (36,36))
tile_0116 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0116.png'), (36,36))
tile_0047 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0047.png'), (36,36))
tile_0037 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0037.png'), (36,36))
tile_0038 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0038.png'), (36,36))
tile_0039 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0039.png'), (36,36))
tile_0104 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0104.png'), (36,36))
tile_0111 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0111.png'), (36,36))
tile_0057 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0057.png'), (36,36))
tile_0097 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0097.png'), (36,36))
tile_0059 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0059.png'), (36,36))
tile_0026 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0026.png'), (36,36))
tile_0131 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0131.png'), (36,36))
tile_0117 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0117.png'), (36,36))
tile_0137 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0137.png'), (36,36))
tile_0126 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0126.png'), (36,36))
tile_0128 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0128.png'), (36,36))
tile_0024 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0024.png'), (36,36))
tile_0025 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0025.png'), (36,36))
tile_0112 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0112.png'), (36,36))
tile_0048 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0048.png'), (36,36))
tile_0049 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0049.png'), (36,36))
tile_0050 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0050.png'), (36,36))
tile_0029 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0029.png'), (36,36))
tile_0064 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0064.png'), (36,36))
tile_0127 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0127.png'), (36,36))
tile_0006 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0006.png'), (36,36))
tile_0061 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0061.png'), (36,36))
tile_0062 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0062.png'), (36,36))
tile_0063 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0063.png'), (36,36))
tile_0041 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0041.png'), (36,36))
tile_0042 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0042.png'), (36,36))
tile_0043 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0043.png'), (36,36))
tile_0066 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0066.png'), (36,36))
tile_0004 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0004.png'), (36,36))
tile_0089 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0089.png'), (36,36))
tile_0098 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0098.png'), (36,36))
tile_0076 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0076.png'), (36,36))
tile_0056 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0056.png'), (36,36))
tile_0129 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0129.png'), (36,36))
tile_0005 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0005.png'), (36,36))
tile_0009 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0009.png'), (36,36))
tile_0010 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0010.png'), (36,36))
tile_0028 = pygame.transform.scale(pygame.image.load('Tileset/Tiles/tile_0028.png'), (36,36))

tile_rects = []
win_tile_rects = []
lever_rect = []
tiles = [tile_0021,tile_0022,tile_0023,tile_0121,tile_0122,tile_0123,tile_0141,tile_0142,tile_0143,tile_0001,tile_0002,tile_0003,tile_0047,tile_0104,tile_0026,tile_0024,tile_0025,tile_0048,tile_0049,
         tile_0050,tile_0029,tile_0006,tile_0061,tile_0062,tile_0063,tile_0041,tile_0042,tile_0043,tile_0004,tile_0098,tile_0005,tile_0009,tile_0010,tile_0028]
transparent_tiles= [tile_0124,tile_0125,tile_0088,tile_0017,tile_0018,tile_0019,tile_0116,tile_0037,tile_0038,tile_0039,tile_0111,tile_0057,tile_0097,tile_0059,tile_0131,tile_0117,tile_0137,tile_0126,
                    tile_0128,tile_0112,tile_0064,tile_0127,tile_0066, tile_0076,tile_0056,tile_0129,tile_0089]
def draw_board(board,surface):
    for i in range(len(board)):
        for j in range (len(board[i])):
            value = board[i][j]
            if value != -1:
                if value == 21:
                    surface.blit(tiles[0], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 22:
                    surface.blit(tiles[1], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 23:
                    surface.blit(tiles[2], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 121:
                    surface.blit(tiles[3], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 122:
                    surface.blit(tiles[4], (j*TILESIZE, i*TILESIZE))
                elif value == 123:
                    surface.blit(tiles[5], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 124:
                    surface.blit(transparent_tiles[0], (j*TILESIZE, i*TILESIZE))
                elif value == 125:
                    surface.blit(transparent_tiles[1], (j*TILESIZE, i*TILESIZE))
                elif value == 141:
                    surface.blit(tiles[6], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 142:
                    surface.blit(tiles[7], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 143:
                    surface.blit(tiles[8], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 88:
                    surface.blit(transparent_tiles[2], (j*TILESIZE, i*TILESIZE))
                elif value == 1:
                    surface.blit(tiles[9], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 2:
                    surface.blit(tiles[10], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 3:
                    surface.blit(tiles[11], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 17:
                    surface.blit(transparent_tiles[3], (j*TILESIZE, i*TILESIZE))
                elif value == 18:
                    surface.blit(transparent_tiles[4], (j*TILESIZE, i*TILESIZE))
                elif value == 19:
                    surface.blit(transparent_tiles[5], (j*TILESIZE, i*TILESIZE))
                elif value == 116:
                    surface.blit(transparent_tiles[6], (j*TILESIZE, i*TILESIZE))
                elif value == 47:
                    surface.blit(tiles[12], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 37:
                    surface.blit(transparent_tiles[7], (j*TILESIZE, i*TILESIZE))
                elif value == 38:
                    surface.blit(transparent_tiles[8], (j*TILESIZE, i*TILESIZE))
                elif value == 39:
                    surface.blit(transparent_tiles[9], (j*TILESIZE, i*TILESIZE))
                elif value == 104:
                    surface.blit(tiles[13], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 111:
                    surface.blit(transparent_tiles[10], (j*TILESIZE, i*TILESIZE))
                    win_tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 57:
                    surface.blit(transparent_tiles[11], (j*TILESIZE, i*TILESIZE))
                elif value == 97:
                    surface.blit(transparent_tiles[12], (j*TILESIZE, i*TILESIZE))
                elif value == 59:
                    surface.blit(transparent_tiles[13], (j*TILESIZE, i*TILESIZE))
                elif value == 26:
                    surface.blit(tiles[14], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 131:
                    surface.blit(transparent_tiles[14], (j*TILESIZE, i*TILESIZE))
                    win_tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 117:
                    surface.blit(transparent_tiles[15], (j*TILESIZE, i*TILESIZE))
                elif value == 137:
                    surface.blit(transparent_tiles[16], (j*TILESIZE, i*TILESIZE))
                elif value == 126:
                    surface.blit(transparent_tiles[17], (j*TILESIZE, i*TILESIZE))
                elif value == 128:
                    surface.blit(transparent_tiles[18], (j*TILESIZE, i*TILESIZE))
                elif value == 24:
                    surface.blit(tiles[15], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 25:
                    surface.blit(tiles[16], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 112:
                    surface.blit(transparent_tiles[19], (j*TILESIZE, i*TILESIZE))
                    win_tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 48:
                    surface.blit(tiles[17], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 49:
                    surface.blit(tiles[18], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 50:
                    surface.blit(tiles[19], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 29:
                    surface.blit(tiles[20], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 64:
                    surface.blit(transparent_tiles[20], (j*TILESIZE, i*TILESIZE))
                    lever_rect.append(pygame.Rect((j*TILESIZE)-(TILESIZE/2), i*TILESIZE, TILESIZE*2, TILESIZE))
                elif value == 127:
                    surface.blit(transparent_tiles[21], (j*TILESIZE, i*TILESIZE))
                    lever_rect.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 6:
                    surface.blit(tiles[21], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 61:
                    surface.blit(tiles[22], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 62:
                    surface.blit(tiles[23], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 63:
                    surface.blit(tiles[24], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 41:
                    surface.blit(tiles[25], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 42:
                    surface.blit(tiles[26], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 43:
                    surface.blit(tiles[27], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 66:
                    surface.blit(transparent_tiles[22], (j*TILESIZE, i*TILESIZE))
                elif value == 4:
                    surface.blit(tiles[28], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 98:
                    surface.blit(tiles[29], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 76:
                    surface.blit(transparent_tiles[23], (j*TILESIZE, i*TILESIZE))
                elif value == 56:
                    surface.blit(transparent_tiles[24], (j*TILESIZE, i*TILESIZE))
                elif value == 129:
                    surface.blit(transparent_tiles[25], (j*TILESIZE, i*TILESIZE))
                elif value == 5:
                    surface.blit(tiles[30], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 9:
                    surface.blit(tiles[31], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 10:
                    surface.blit(tiles[32], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 28:
                    surface.blit(tiles[33], (j*TILESIZE, i*TILESIZE))
                    tile_rects.append(pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE))
                elif value == 89:
                    surface.blit(transparent_tiles[26], (j*TILESIZE, i*TILESIZE))
                else:
                    pass
                
    
                
                
            