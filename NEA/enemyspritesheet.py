#############ENEMY SPRITESHEET##########
import pygame
def get_image(spritesheet, width, height,layer,scale,colour,frame):
    spritesheet = pygame.transform.scale(spritesheet, (spritesheet.get_width()*scale,spritesheet.get_height()*scale))
    image = pygame.Surface((width*scale,height*scale)).convert_alpha()
    image.fill(colour)
    image.blit(spritesheet, (0,0), (frame*width*scale,layer*scale,width*scale, height*scale))
    image.set_colorkey(colour)
    return image
