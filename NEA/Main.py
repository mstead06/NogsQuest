#Main Script
import pygame, tiles,sprites, spritesheet, levels
pygame.init()
#Constants

FPS = 60
WIDTH,HEIGHT = 1152,648
SCREEN_DIMENSIONS = pygame.Vector2(1152,648)
TILE_DIMENSIONS = pygame.Vector2(36,36)
MAIN_BG = pygame.image.load('Main BG.jpg')
MAIN_BG = pygame.transform.scale(MAIN_BG,SCREEN_DIMENSIONS)
DESERT_BG = pygame.image.load('Desert BG.jpg')
DESERT_BG = pygame.transform.scale(DESERT_BG,SCREEN_DIMENSIONS)
CAVE_BG = pygame.image.load('CAVE_BG.png')
CAVE_BG = pygame.transform.scale(CAVE_BG,SCREEN_DIMENSIONS)
window = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Nog's Quest")

FONT = pygame.font.Font('PIXELFONT.ttf', 50)
TITLE = FONT.render("NOG'S QUEST", True, (0,0,0))


START_BTN_WIDTH, START_BTN_HEIGHT = 248, 120
start_btn_sheet = pygame.image.load('start_button_sheet.png')
start_btn = spritesheet.get_image(start_btn_sheet,62,30,4, (0,0,255),0)
start_btn_hover = spritesheet.get_image(start_btn_sheet,62,30,4, (0,0,255),1)
air_ship_stock_img = pygame.image.load('StockAirShip.png')
air_ship_stock = spritesheet.get_image(air_ship_stock_img, 433,230,1.4,(255,255,255),0)
character = sprites.player()

def main():
    pygame.init()
    run = True
    start_screen_run = False
    first_level_run = False
    second_level_run = False
    third_level_run = False
    clock = pygame.time.Clock()
    window.blit(MAIN_BG,(0,0))
    window.blit(air_ship_stock, ((1152/2-432*1.4/2),(35)))
    # draw board tiles
    tiles.draw_board(levels.start_map,window)
    window.blit(TITLE, ((1152/2-220),356))
    start_btn_x, start_btn_y = ((WIDTH/2) - (START_BTN_WIDTH/2)), ((HEIGHT/2) - (START_BTN_HEIGHT/2) + 220)
    window.blit(start_btn, (start_btn_x, start_btn_y))
    move_counter = 0
    move_right = False
    move_left = False
    character.position.x, character.position.y = 36, 422
    while run:
        start_screen_run = True
        while start_screen_run:
            clock.tick(FPS)
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:
                    start_screen_run = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start_screen_run = False
                        run = False
            if ((pygame.mouse.get_pos()[0] <= start_btn_x + START_BTN_WIDTH and  pygame.mouse.get_pos()[0] >= start_btn_x) and (pygame.mouse.get_pos()[1] <= start_btn_y + START_BTN_HEIGHT and  pygame.mouse.get_pos()[1] >= start_btn_y)):
                window.blit(start_btn_hover, (start_btn_x, start_btn_y))
                if pygame.mouse.get_pressed()[0]:
                    start_screen_run = False
                    first_level_run = True
                    tiles.tile_rects = []
                    frame = 0
                    character.draw(window,frame)
                    counter = 15
            else:
                window.blit(start_btn, (start_btn_x, start_btn_y))
            pygame.display.flip()
        while first_level_run:
            dt = clock.tick(60)*0.001*FPS
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:
                    second_level_run = False
                    first_level_run = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY, character.FACING_LEFT = True, True
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY, character.FACING_LEFT = True, False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        character.jump()
                    elif event.key == pygame.K_ESCAPE:
                        first_level_run = False
                        run = False
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY = False
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY = False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        if character.is_jumping:
                            character.velocity.y *= .25
                            character.is_jumping = False
            character.update(dt,tiles.tile_rects)  
            if counter <= 15:
                window.blit(MAIN_BG,(0,0))
                tiles.tile_rects = []
                tiles.draw_board(levels.first_level_frame1,window)  
            elif counter <= 30:
                window.blit(MAIN_BG,(0,0))
                tiles.tile_rects = []
                tiles.draw_board(levels.first_level_frame2,window)
                if counter == 30:
                    counter = 0
            counter +=1

            if character.rect.x < 2:
                character.position.x = 2
            if character.rect.x > 1150-(18*3):
                character.position.x = 1150-(18*3)
            character.draw(window,frame)
            frame+=1
            if frame >= 30:
                frame = 0
            for i in range (len(tiles.win_tile_rects)):
                if character.rect.colliderect(tiles.win_tile_rects[i]):
                    state = 1
                    window.blit(DESERT_BG,(0,0))
                    character.position.x,character.position.y = 36, 422
                    tiles.tile_rects = []
                    win_tile_rects = []
                    character.update(dt,tiles.tile_rects)
                    character.draw(window,frame)
                    first_level_run = False
                    second_level_run = True
                    tiles.draw_board(levels.level2_state1_frame1,window)
                    pygame.time.delay(50)
                    break
                    
                    
            print(str(int(clock.get_fps())))
            pygame.display.flip()
            
        while second_level_run:
            dt = clock.tick(60)*0.001*FPS
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:
                    second_level_run = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY, character.FACING_LEFT = True, True
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY, character.FACING_LEFT = True, False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        character.jump()
                    elif event.key == pygame.K_ESCAPE:
                        second_level_run = False
                        run = False
                    elif event.key == pygame.K_c:
                        if character.rect.colliderect(tiles.lever_rect[0]):
                            if state == 1:
                                state = 2
                            elif state == 2:
                                state = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY = False
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY = False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        if character.is_jumping:
                            character.velocity.y *= .25
                            character.is_jumping = False
            for i in range (len(tiles.win_tile_rects)):
                if character.rect.colliderect(tiles.win_tile_rects[i]):
                    win_tile_rects = []
                    state = 1
                    window.blit(CAVE_BG,(0,0))
                    character.position.x,character.position.y = 36, 422
                    tiles.tile_rects = []
                    win_tile_rects = []
                    character.update(dt,tiles.tile_rects)
                    character.draw(window,frame)
                    second_level_run = False
                    third_level_run = True
                    tiles.draw_board(levels.level3_state1_frame1,window)
                    key = sprites.consumable(0)
                    key.draw(window)
                    pygame.time.delay(50)
                    break
            character.update(dt,tiles.tile_rects)
            if state == 1:
                if counter <= 15:
                    window.blit(DESERT_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state1_frame1,window)
                elif counter <= 30:
                    window.blit(DESERT_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state1_frame2,window)
            elif state == 2:
                if counter <= 15:
                    window.blit(DESERT_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state2_frame1,window)
                elif counter <= 30:
                    window.blit(DESERT_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state2_frame2,window)
            
            if counter == 30:
                counter = 0                
            counter +=1
            frame+=1
            if frame >= 30:
                frame = 0
            print(str(int(clock.get_fps())))
            character.draw(window,frame)
            if character.rect.x < 2:
                character.position.x = 2
            if character.rect.x > 1150-(18*3):
                character.position.x = 1150-(18*3)
            pygame.display.flip()
            
        while third_level_run:
            dt = clock.tick(60)*0.001*FPS
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:
                    third_level_run = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY, character.FACING_LEFT = True, True
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY, character.FACING_LEFT = True, False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        character.jump()
                    elif event.key == pygame.K_ESCAPE:
                        second_level_run = False
                        run = False
                    elif event.key == pygame.K_c:
                        if character.rect.colliderect(tiles.lever_rect[0]):
                            if state == 1:
                                state = 2
                            elif state == 2:
                                state = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        character.LEFT_KEY = False
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        character.RIGHT_KEY = False
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        if character.is_jumping:
                            character.velocity.y *= .25
                            character.is_jumping = False
            
            for i in range (len(tiles.win_tile_rects)):
                if character.rect.colliderect(tiles.win_tile_rects[i]):
                    print("WIN")
                    break
            character.update(dt,tiles.tile_rects)
            if state == 1:
                if counter <= 15:
                    window.blit(CAVE_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level3_state1_frame1,window)
                elif counter <= 30:
                    window.blit(CAVE_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level3_state1_frame2,window)
            elif state == 2:
                if counter <= 15:
                    window.blit(CAVE_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state2_frame1,window)
                elif counter <= 30:
                    window.blit(CAVE_BG,(0,0))
                    tiles.tile_rects = []
                    tiles.draw_board(levels.level2_state2_frame2,window)
            
            if counter == 30:
                counter = 0                
            counter +=1
            frame+=1
            if frame >= 30:
                frame = 0
            print(str(int(clock.get_fps())))
            character.draw(window,frame)
            if character.rect.x < 2:
                character.position.x = 2
            if character.rect.x > 1150-(18*3):
                character.position.x = 1150-(18*3)
            pygame.display.flip()
            
            
    pygame.display.quit()
        
main()
