# importing the library
import pygame

# initializing all the imported
# pygame modules
x = pygame.init()

# printing the number of modules
# initialized successfully
#print(x)

#creating display window
gamewindow = pygame.display.set_mode((600,500))


# getsize from user
# x,y = gamewindow.get_size()

# pygame.display.quit()
pygame.display.set_caption('Flappy bird')   # change the name of the window
# Here we load the image we want to
# use
Icon = pygame.image.load('flappy.png')

# We use set_icon to set new icon
pygame.display.set_icon(Icon)
#gamewindow.fill((0,0,255))                  # set colour using fill and display.flip()
pygame.display.flip()
running = True

color = "red"
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		gamewindow.fill(color)
		pygame.display.flip()
		# if color=='red':
		# 	color='green'
		# else:
		# 	color = 'red'
		#pygame.draw.circle(gamewindow,(0,0,0),(300,200),75)
		pygame.display.update()


pygame.QUIT()