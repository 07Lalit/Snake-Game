import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# colors:
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# creating window
screen_width = 700
screen_height = 500

#background image


# title and window
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    window.blit(screen_text,[x,y])

def plot_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

def welcome():
    running = True
    while running:
        window.fill((213,220,239))
        text_screen("Welcome to Snake Game",black,100,150)
        text_screen("Press Space Bar to play", black, 120,200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('snake_music.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)

# game loop
def gameloop():
    # game specific variable
    running = True
    game_over= False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(30, screen_height // 2)
    score = 0
    fps = 46
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_list = []
    snake_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("40")

    with open("highscore.txt", "r") as f:
        hs = f.read()

    while running:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hs))
            window.fill(white)
            text_screen("Game Over ! Press Enter to continue",red,10 , 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y =0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x)<16 and abs(snake_y - food_y)<16:
                score += 10
                food_x = random.randint(20, screen_width//2)
                food_y = random.randint(30, screen_height//2)
                snake_length+=5
                if score > int(hs):
                    hs = score


            window.fill(white)
            window.blit(bgimg,(0,0))
            text_screen(f"score : {score} High Score: {hs}", red, 5, 5)
            pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)> snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over= True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y >screen_height :
                game_over = True
                pygame.mixer.music.load('game_over.mp3')
                pygame.mixer.music.play()
                #print("game over")
            #pygame.draw.rect(window,black,[snake_x,snake_y,snake_size,snake_size])  # (kha bnoge, kis color,[x,y,length,widht])
            plot_snake(window,black,snake_list,snake_size)
            # change in event update using update function
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

#gameloop()
welcome()