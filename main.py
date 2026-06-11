import pygame
from math import sin, cos

pygame.init()

speed = 10

WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


class Car:
    def __init__(self):
        self.pos = [0, 0]
        self.velo = [0, 0]
        self.angle = 0
        self.direction = [cos(self.angle), sin(self.angle)]
        self.speed = 10
        self.carImage = pygame.image.load("F1Car.png").convert_alpha()
        self.carRect = self.carImage.get_rect(center = self.pos)
    def draw(self):
        self.carRect = self.carImage.get_rect(center = self.pos)
        screen.blit(self.carImage, self.carRect)

carOne = Car()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                carOne.pos[1] -= carOne.speed
            if event.key == pygame.K_DOWN:
                carOne.pos[1] += carOne.speed
            if event.key == pygame.K_LEFT:
                carOne.pos[0] -= carOne.speed
            if event.key == pygame.K_RIGHT:
                carOne.pos[0] += carOne.speed
    screen.fill((10, 10, 10))
    carOne.draw()
    pygame.display.flip()
pygame.quit()