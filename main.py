import pygame
import player
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class MAIN:
    def __init__(self):
        self.player_circle = player.PLAYER(screen)

    def draw_elements(self):
        self.player_circle.draw_player()

    def update(self):
        self.player_circle.move_player(dt)

main_game = MAIN()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")
    main_game.draw_elements()
    pygame.display.update()
    main_game.update()
    dt = clock.tick(60) / 1000

pygame.quit()