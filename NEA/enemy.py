###########ENEMIES#####################
import pygame,random,enemyspritesheet

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        enemies = pygame.image.load('enemies.png')
        pygame.sprite.Sprite.__init__(self)
        enemy_type = (random.randint(0,11)*19)
        self.image = enemyspritesheet.get_image(enemies, 16, 19,enemy_type,8,(0,0,0),0).convert_alpha()
        self.rect = self.image.get_rect()
    def draw(self,display):
        display.blit(self.image, (self.rect.x, self.rect.y))
    
#test delete later

FPS = 60
WIDTH,HEIGHT = 1152,648
SCREEN_DIMENSIONS = pygame.Vector2(1152,648)
TILE_DIMENSIONS = pygame.Vector2(36,36)
MAIN_BG = pygame.image.load('Main BG.jpg')
MAIN_BG = pygame.transform.scale(MAIN_BG,SCREEN_DIMENSIONS)
run = 1
window = pygame.display.set_mode(SCREEN_DIMENSIONS)
while run:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            start_screen_run = False
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                window.fill((0,0,0))
                Enemy = enemy()
                Enemy.draw(window)
    pygame.display.update()       
        
        