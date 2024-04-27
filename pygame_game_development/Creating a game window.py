import pygame   # import pygame
pygame.init()   # initialization of all module

#Creating window
window = pygame.display.set_mode((1200,500))
# Giving name to window
pygame.display.set_caption("My First Game ")

# Game specific variable
exit_game = True
game_over = True

# crating game loop  (jab tak game chalta rahega tab tak loop chalega
# sarre events ko handle karega keyword mouse , joystick
# update in the game

while exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            elif event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")
            elif event.key == pygame.K_UP:
                print("You have pressed UP arrow key")
            elif event.key == pygame.K_DOWN:
                print("You have pressed down arrow key")



pygame.quit()
quit()