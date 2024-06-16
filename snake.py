#                               PYGAME-Snake

import pygame
import random 
import os

pygame.mixer.init()

pygame.init()


'''                         PYGAME VARIABLES                       '''

# Colors(R, G, B)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# CREATING WINDOW  /  this is how we create game/display window
screen_width = 1000
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Backgroung image
bgimg = pygame.image.load('/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/backgroundsnake.png')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# to title the game we use set_caption
pygame.display.set_caption("SNAKE Game")

# Game specific variables
exit_game = False
game_over= False

# clock for velocities, fps and other stuff
fps = 30
clock = pygame.time.Clock()

# snake
snake_x = 45
snake_y = 45
snake_size = 20
velocity_x = 0
velocity_y = 0
init_velocity = 7
snk_list = []
snk_length = 1

# Snake Head image
headimg = pygame.image.load('/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/snakehead.png')
headimg = pygame.transform.scale(headimg, (snake_size, snake_size)).convert_alpha()

# food
food_x = random.randint(10, screen_width//1.2)
food_y = random.randint(10, screen_height//1.2) 
food_size = 15

# distance difference
gap_x = 10
gap_y = 10

# score
score = 0
font = pygame.font.SysFont(None, 50)


def text_screen(text, color, x, y):
    
    # to display font we use render function of font in pygame
    screen_text = font.render(text, True, color)
        # for dispaly
        #        .blit(where, [coordinates])
        #               |           |
        #               |           |
        #               v           v
    gameWindow.blit(screen_text, [x, y])


def plot_snake(where, color, list, size):
    for x, y in snk_list:
        pygame.draw.rect(where, color, [x, y, snake_size, snake_size])

def welcome():
    global exit_game
    global fps
    global clock
    global black 
    global green

    exit_welcome = False
    while not exit_welcome:
        gameWindow.fill(white)
        text_screen("                   Welcome To Snakes       ", black, screen_width//8, screen_height//3)
        text_screen("                     Enter spacebar to start     ", green, screen_width//10, screen_height//2.5 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                exit_welcome = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(fps)


def gameloop():
    
    #                               GLOBAL VARIABLE 
    #
    global white
    global red
    global blue
    #
    global screen_height
    global screen_width
    #
    global exit_game
    global game_over
    #
    global fps
    global clock
    #
    global snake_x
    global snake_y
    global snake_size
    global snk_length
    global snk_list
    global velocity_x
    global velocity_y
    global init_velocity
    #
    global food_x
    global food_y
    global food_size
    #
    global gap_x
    global gap_y
    #
    global score
    

    # highscore
    if(not os.path.exists("/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/highscore.txt")):
        with open("/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/highscore.txt", "w") as f:
            f.write("0")
 
    with open("/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/highscore.txt", "r") as f:
        high_score = f.read()
        high_score = int(high_score)


    # Creating a game loop to stop window to close instantly
    while not exit_game:
        
        if game_over:
            with open("/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/highscore.txt", "w") as f:
                f.write(str(high_score))

            gameWindow.fill(black)
            text_screen("GAME OVER PRESS ENTER TO CONTINUE", red, screen_width//9, screen_height//4)
            text_screen("Your Score: "+ str(score) + "    High Score: "+ str(high_score) , blue, screen_width//10, screen_height//2)
            

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
        
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        score = 0
                        gameloop()

        else:

            # Creating Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                # to get keys input we use KEYDOWN 
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -(init_velocity)
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -(init_velocity)
                        velocity_x = 0
        
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_a:
                        velocity_x = -(init_velocity)
                        velocity_y = 0

                    if event.key == pygame.K_w:
                        velocity_y = -(init_velocity)
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

                    
                    if event.key == pygame.K_q:
                        gap_x = 30
                        gap_y = 30
                    

                    if event.key == pygame.K_e:
                        gap_x = 10
                        gap_y = 10

            
            # system of movement of snake
            snake_x += velocity_x
            snake_y += velocity_y

            #                            Score Algorithm
            if abs(snake_x - food_x) < gap_x and abs(snake_y - food_y) < gap_y:
                pygame.mixer.music.load('/Users/manishshivach/Documents/VSCode/Python/Mini Projects/snake/beep.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(10, screen_width//1.2)
                food_y = random.randint(10, screen_height//1.2)
                snk_length += 5

                if score > high_score:
                    high_score = score


            # Background Color and Image
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            
            # Score display
            text_screen("Score: "+ str(score) + "    High Score: "+ str(high_score) , blue, 5, 5)
            

            # Food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])   
            

            # Algorithm for snake length
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                velocity_x = 0
                velocity_y = 0
                del head
                del snk_list
                del snk_length
                snake_x = 45
                snake_y = 45
                snk_length = 0
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list = []
                snk_list.append(head)

                game_over = True
            
            if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height:
                velocity_x = 0
                velocity_y = 0
                del head
                del snk_list
                del snk_length
                snake_x = 45
                snake_y = 45
                snk_length = 0
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list = []
                snk_list.append(head)

                game_over = True
            
            plot_snake(gameWindow, white, snk_list, snake_size)
            gameWindow.blit(headimg, (snake_x, snake_y))

        pygame.display.update()
        clock.tick(fps)


    pygame.display.quit()
    quit()


welcome()
