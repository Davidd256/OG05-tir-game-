#Разработаем кейс: игру «Тир» с использованием библиотеки Pygame.
import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/TIR2.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/Apple.jpg")
target_width = 80
target_height = 120
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()
