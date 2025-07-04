import pygame
import math



class PLAYER:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 40
        self.spawn_location = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 100)
        self.font = pygame.font.Font('Worktalk.ttf', 32)
        self.direction = True
        self.speed = 300
        self.score = 0

    def draw_player(self):
        player_cir = pygame.draw.circle(self.screen, "red", self.spawn_location, self.radius)
        score_text = self.font.render(str(math.floor(self.score)), True, "white")
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (int(self.spawn_location.x), int(self.spawn_location.y))
        self.screen.blit(score_text, score_text_rect)

    def move_player(self, dt):
        if self.spawn_location.x >= self.screen.get_width() - 20:
            self.direction = False
        elif self.spawn_location.x <= 20:
            self.direction = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.speed = 0
        elif keys[pygame.K_w]:
            self.speed = 750
        else:
            self.speed = 300



        if self.direction:
            self.spawn_location.x += self.speed * dt
        else:
            self.spawn_location.x -= self.speed * dt
