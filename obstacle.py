import pygame
import random
import math

class OBSTACLE:
    def __init__(self, screen):
        self.screen = screen
        self.distance = 300
        self.width = int(math.floor(self.screen.get_width()))
        self.height = 20
        self.obstacle1_location = pygame.Vector2(-self.width / 2, 0)
        self.obstacle2_location = pygame.Vector2(self.obstacle1_location.x + self.width + self.distance, 0)
        self.speed = 250


    def draw_obstacle(self):
        obstacle1_rect = pygame.Rect(self.obstacle1_location.x, self.obstacle1_location.y, self.width, self.height)
        obstacle2_rect = pygame.Rect(self.obstacle2_location.x, self.obstacle2_location.y, self.width, self.height)
        pygame.draw.rect(self.screen, "gray", obstacle1_rect)
        pygame.draw.rect(self.screen, "gray", obstacle2_rect)

    def move_obstacles(self, dt):
        self.obstacle1_location.y += self.speed * dt
        self.obstacle2_location.y += self.speed * dt

        if self.obstacle1_location.y >= self.screen.get_height() + self.height:
            self.obstacle1_location.y = -self.height
            self.obstacle2_location.y = -self.height

            self.obstacle1_location.x = random.randint(int(-self.width), int(-self.width / 6))
            self.obstacle2_location.x = self.obstacle1_location.x + self.width + self.distance


    def check_collision(self, circle_pos, radius):
        obstacle1_rect = pygame.Rect(self.obstacle1_location.x, self.obstacle1_location.y, self.width, self.height)
        obstacle2_rect = pygame.Rect(self.obstacle2_location.x, self.obstacle2_location.y, self.width, self.height)

        return self.circle_rect_collision(circle_pos, radius, obstacle1_rect) or self.circle_rect_collision(circle_pos, radius, obstacle2_rect)

    @staticmethod
    def circle_rect_collision(circle_pos, radius, rect):
        closest_x = max(rect.left, min(circle_pos.x, rect.right))
        closest_y = max(rect.top, min(circle_pos.y, rect.bottom))

        distance_x = circle_pos.x - closest_x
        distance_y = circle_pos.y - closest_y

        return (distance_x**2 + distance_y**2) < (radius**2)