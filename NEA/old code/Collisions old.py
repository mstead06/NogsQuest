###################Collisions###################
def collision_test(rect, tiles):
    hitlist = []
    for tile in tiles:
        if rect.colliderect(tile):
            hitlist.append(tile)
    return hitlist

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hitlist = collision_test(rect,tiles)
    for tile in hitlist:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hitlist = collision_test(rect,tiles)
    for tile in hitlist:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True    
    return rect, collision_types