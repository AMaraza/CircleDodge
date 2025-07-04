import pygame
import player
import obstacle
import math
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class MAIN:
    def __init__(self):
        self.score_text_rect = None
        self.score_text = None
        self.player_circle = player.PLAYER(screen)
        self.obstacles = obstacle.OBSTACLE(screen)
        self.temp_score = 0
        self.high_score = 0
        self.font = pygame.font.Font('Worktalk.ttf', 32)



    def draw_elements(self):
        self.player_circle.draw_player()
        self.obstacles.draw_obstacle()
        self.score_text = self.font.render(f"Best: {str(math.floor(self.high_score))}", True, "white")
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (100, 50)
        screen.blit(self.score_text, self.score_text_rect)

    def update(self):
        self.player_circle.move_player(dt)
        self.obstacles.move_obstacles(dt)

        if self.obstacles.check_collision(self.player_circle.spawn_location, self.player_circle.radius):
            if self.player_circle.score > self.high_score:
                self.high_score = self.player_circle.score
            self.player_circle.score = 0
            self.obstacles.speed = 250
            self.temp_score = 0

        else:
            self.player_circle.score += 1 * dt

        if self.player_circle.score >= self.temp_score + 20:
            self.obstacles.speed *= 1.3
            self.temp_score = self.player_circle.score

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