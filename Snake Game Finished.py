import pygame, time, random
#x = pygame.init()
#print(x)
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False


FPS = 30
blockSize = 10
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 25)

def messageToScreen(msg,color):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth/2,displayHeight/2])
    
def gameLoop():
    gameExit = False
    gameOver = False
    
    speedX = 0
    speedY = 0
    
    leadX = displayWidth/2
    leadY = displayHeight/2

    randAppleX = round(random.randrange(0,displayWidth-blockSize)/10.0)*10.0
    randAppleY = round(random.randrange(0,displayHeight-blockSize)/10.0)*10.0
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            messageToScreen('Game Over, press C to play again Q to quit',red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
    #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speedX = -blockSize
                    speedY = 0
                if event.key == pygame.K_RIGHT:
                    speedX = blockSize
                    speedY = 0
                if event.key == pygame.K_UP:
                    speedY = -blockSize
                    speedX = 0
                if event.key == pygame.K_DOWN:
                    speedY = blockSize
                    speedX = 0
    #boundary conditons
        if leadX<=0 or leadY<=0 or leadX>=displayWidth-20 or leadY>=displayHeight:
            gameOver = True
                
                    
        gameDisplay.fill(white)
    #Location processing
        leadX = leadX + speedX
        leadY = leadY + speedY
    #Graphics rendering
        pygame.draw.rect(gameDisplay,black,[randAppleX,randAppleY,blockSize,blockSize])
        pygame.draw.rect(gameDisplay,red,[leadX,leadY,blockSize,blockSize])
        pygame.display.update() # updates whatever graphical actions we performed

        if leadX == randAppleX and leadY == randAppleY:
            print('yummmmmmmy')
            

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
