import pygame

pygame.init()

canvas = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Reporte")
clock = pygame.time.Clock()

pygame.display.flip()
running = True

dt = 1
gravity = 1
player_position = pygame.Vector2(canvas.get_width() / 2, canvas.get_height() / 2)
player_velocity = pygame.Vector2(0,0)
background = pygame.image.load("sunset.png")
on_ground = False

def physics(player_position, player_velocity, gravity):
    global on_ground

    if player_velocity.y < 20:
        player_velocity.y += gravity * dt
    else:
        player_velocity.y = 20

    if ground.colliderect(player):
        on_ground = True
    else:
        on_ground = False

    player_position += player_velocity * dt

def friction(player_velocity):
    global on_ground
    if on_ground:
        player_velocity.x = player_velocity.x * 4/5

def move_sideways(player_position, player_velocity, acceleration, direction):
    if direction.lower().strip() == "l":
        player_velocity.x -= acceleration * dt
    elif direction.lower().strip() == "r":
        player_velocity.x += acceleration * dt

    if player_velocity.x > 5:
        player_velocity.x = 5

    if player_velocity.x < -5:
        player_velocity.x = -5
    player_position += player_velocity * dt

def check_ground_collision(player, ground):
    global player_position

    if on_ground:
        player.bottom = ground.top
        player_position.y = player.y
        player_velocity.y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    canvas.blit(background, (0, 0))

    # RENDER YOUR GAME HERE
    player = pygame.Rect(player_position.x, player_position.y, 10, 10)
    ground = pygame.Rect(0, 448, 800, 152)

    physics(player_position, player_velocity, gravity)
    check_ground_collision(player, ground)
    friction(player_velocity)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and on_ground:
        player_velocity.y -= 15 * dt
    if keys[pygame.K_a]:
        # player_position.x -= 15 * dt
        move_sideways(player_position, player_velocity, 3, "l")
    if keys[pygame.K_d]:
        # player_position.x += 15 * dt
        move_sideways(player_position, player_velocity, 3, "r")

    '''
    if keys[pygame.K_a] and not on_ground:
        move_sideways(player_position, player_velocity, 1, "a")
    if keys[pygame.K_d] and not on_ground:
        move_sideways(player_position, player_velocity, 1, "d")
    '''

    pygame.draw.rect(canvas, "white", player)

    # flip() the display to put your work on screen®
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()