############################SPRITES#############################
import pygame, spritesheet

class player(pygame.sprite.Sprite):
    def __init__(self):
        character_walk_right = pygame.image.load('character walk right.png')
        character_walk_left = pygame.image.load('character walk left.png')
        character_jump = pygame.image.load('character jump.png')
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),0).convert_alpha()
        self.image_walk_right1 = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),0).convert_alpha()
        self.image_walk_right2 = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),1).convert_alpha()
        self.image_walk_right3 = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),2).convert_alpha()
        self.image_walk_right4 = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),3).convert_alpha()
        self.image_walk_right5 = spritesheet.get_image(character_walk_right, 14, 18,3,(0,0,0),4).convert_alpha()
        self.image_walk_left1 = spritesheet.get_image(character_walk_left, 14, 18,3,(0,0,0),0).convert_alpha()
        self.image_walk_left2 = spritesheet.get_image(character_walk_left, 14, 18,3,(0,0,0),1).convert_alpha()
        self.image_walk_left3 = spritesheet.get_image(character_walk_left, 14, 18,3,(0,0,0),2).convert_alpha()
        self.image_walk_left4 = spritesheet.get_image(character_walk_left, 14, 18,3,(0,0,0),3).convert_alpha()
        self.image_walk_left5 = spritesheet.get_image(character_walk_left, 14, 18,3,(0,0,0),4).convert_alpha()
        self.image_jump_left = spritesheet.get_image(character_jump, 15, 18,3,(0,0,255),0).convert_alpha()
        self.image_jump_right = spritesheet.get_image(character_jump, 15, 18,3,(0,0,255),1).convert_alpha()
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .25, -.09
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    def draw(self, display,frame):
        if self.on_ground and self.velocity.x > 0:
            if frame <= 6:
                display.blit(self.image_walk_right1, (self.rect.x, self.rect.y))
            elif frame <= 12:
                display.blit(self.image_walk_right2, (self.rect.x, self.rect.y))
            elif frame <= 18:
                display.blit(self.image_walk_right3, (self.rect.x, self.rect.y))
            elif frame <= 24:
                display.blit(self.image_walk_right4, (self.rect.x, self.rect.y))
            elif frame <= 30:
                display.blit(self.image_walk_right5, (self.rect.x, self.rect.y))
        elif self.on_ground and self.velocity.x < 0:
            if frame <= 6:
                display.blit(self.image_walk_left1, (self.rect.x, self.rect.y))
            elif frame <= 12:
                display.blit(self.image_walk_left2, (self.rect.x, self.rect.y))
            elif frame <= 18:
                display.blit(self.image_walk_left3, (self.rect.x, self.rect.y))
            elif frame <= 24:
                display.blit(self.image_walk_left4, (self.rect.x, self.rect.y))
            elif frame <= 30:
                display.blit(self.image_walk_left5, (self.rect.x, self.rect.y))
        elif self.on_ground == False:
            if self.velocity.x >= 0:
                display.blit(self.image_jump_left, (self.rect.x, self.rect.y))
            elif self.velocity.x < 0:
                display.blit(self.image_jump_right, (self.rect.x, self.rect.y))
        else:
            if self.velocity.x > 0:
                display.blit(self.image_walk_right1, (self.rect.x, self.rect.y))
            elif self.velocity.x < 0:
                display.blit(self.image_walk_left1, (self.rect.x, self.rect.y))
            else:
                display.blit(self.image_walk_right1, (self.rect.x, self.rect.y))

    def update(self, dt, tiles):
        self.horizontal_movement(dt)
        self.checkCollisionsx(tiles)
        self.vertical_movement(dt)
        self.checkCollisionsy(tiles)

    def horizontal_movement(self,dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .38
        elif self.RIGHT_KEY:
            self.acceleration.x += .38
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(6)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

    def vertical_movement(self,dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7:
            self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):       
        if self.on_ground:
            self.velocity.y = 1.2
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False

    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionsx(self, tiles):
        collisions = self.get_hits(tiles)
        
        for tile in collisions:
            if self.velocity.x > 0:  # Hit tile moving right#
                self.position.x = tile.left - self.rect.w
                self.rect.x = self.position.x
                self.on_ground = True # Can wall jump
                self.velocity.y = 0.86 # Can slide down walls
               
            elif self.velocity.x < 0:  # Hit tile moving left
                self.position.x = tile.right
                self.rect.x = self.position.x
                self.on_ground = True # Can wall jump
                self.velocity.y = 0.86 # Can slide down walls
                
    def checkCollisionsy(self, tiles):
        self.rect.bottom += 1
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:  # Hit tile from the top
                self.on_ground = True
                self.is_jumping = False
                self.velocity.y = 0
                self.position.y = tile.top
                self.rect.bottom = self.position.y
            elif self.velocity.y < 0:  # Hit tile from the bottom
                self.velocity.y = 0
                self.position.y = tile.bottom + self.rect.h
                self.rect.bottom = self.position.y
                

            
        





