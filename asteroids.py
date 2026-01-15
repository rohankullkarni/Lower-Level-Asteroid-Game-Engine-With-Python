#LIBRARIES
import pygame
import numpy as np

pygame.init()


#VARIABLES
running = True
screen = pygame.display.set_mode((640,640))

spaceship = pygame.image.load('spaceship.jpg').convert()
spaceship = pygame.transform.scale(spaceship,(spaceship.get_width()*0.5,spaceship.get_height()*0.5))
bg = pygame.Surface(spaceship.get_size(), pygame.SRCALPHA)
bg.fill((0, 0, 0))
bg.blit(spaceship, (0, 0))
rocks = pygame.image.load('OIP.jpg').convert()
x=250
clock = pygame.time.Clock()
moving_left = False
moving_right = False
rocks_img = pygame.image.load('OIP.jpg').convert_alpha()
rocks_img = pygame.transform.scale(rocks_img, (50, 50))
rocks_arr = []  # list of rock rects
rock_speed = 400  # pixels per second
spawn_delay = 700  # milliseconds
last_spawn = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 36)
game_over_time = 0
game_over = False
GAME_OVER_DELAY = 3






#game loop
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(x,450))
    spaceship.set_colorkey((0,0,0))
    spaceship_rect = bg.get_rect(topleft=(x, 450))

    #rock spawning 
    current_time = pygame.time.get_ticks()
    score = (current_time - start_time) // 1000  # seconds 
    score_text = font.render(f"Time: {score}s", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))



    if current_time - last_spawn > spawn_delay:
        rock_x = np.random.randint(0, 640 - rocks_img.get_width())
        rock_rect = rocks_img.get_rect(topleft=(rock_x, -50))
        rocks_arr.append(rock_rect)
        last_spawn = current_time
    
    for rock in rocks_arr[:]:
        rock.y +=rock_speed * time_delta
        screen.blit(rocks_img, rock)
        if rock.top > 640:
            rocks_arr.remove(rock)
    
    for rock in rocks_arr:
        if spaceship_rect.colliderect(rock):
            game_over = True # stop the game
            game_over_time = pygame.time.get_ticks()
            final_score = score

    if game_over:
        score_text = font.render(f"your final score is:{final_score}",True,)
        screen.blit(score_text,(10,10))
        if pygame.time.get_ticks() - game_over_time >= GAME_OVER_DELAY:
            running = False




    if moving_left:
        x -= 400 *time_delta
    if moving_right:
        x += 400*time_delta


    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right =True
            if event.key == pygame.K_a:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False


    time_delta = clock.tick(60)/1000
    time_delta = max(0.001,min(0.1,time_delta))
    pygame.display.flip()
pygame.quit()