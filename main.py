import pygame, time
from pygame import mixer


#screen
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0, 0, 0))

#square
squareimage = pygame.transform.scale(pygame.image.load("square.png"), (32, 32))
squareX = 150
squareY = 332
squareXmove = 0

def square(x, y):
    screen.blit(squareimage, (x, y))

#triangle
triangleimage = pygame.transform.scale(pygame.image.load("triangle.png"), (64, 64))
triangleX = 350
triangleY = 300

def triangle(x, y):
    screen.blit(triangleimage, (x, y))

#main
running = True
while running == True:

    screen.fill((0, 0, 0))  #leave this line above all in the while loop

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                squareXmove = -10
            if i.key == pygame.K_RIGHT:
                squareXmove = 10
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                squareXmove = 0

        squareX += squareXmove

        if squareimage.get_rect(x=squareX, y=squareY).colliderect(triangleimage.get_rect(x=triangleX, y=triangleY)):
                squareX = -1000
                triangleX = 1000
            

    square(squareX, squareY)
    triangle(triangleX, triangleY)

    pygame.display.update()