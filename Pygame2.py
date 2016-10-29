import pygame
#x = pygame.init()
#print(x)
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)
    #work on other graphics in this space
    #co-ordinates refer to top left
    #(x, y, width, height)
    pygame.draw.rect(gameDisplay,black,[400,300,150,15])
    pygame.draw.rect(gameDisplay,red,[460,300,30,15])
    pygame.display.update() # updates whatever graphical actions we performed












pygame.quit()
quit()
