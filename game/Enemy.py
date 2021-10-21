import random
import game
import pygame


class Enemy:

    def __init__(self):
        self.x_cord = random.randint(100, 1200)
        self.y_cord = 0
        self.image = pygame.image.load("media/hitlerface.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.image.get_width(), self.image.get_height())

    def tick_enemy(self, y_cord):
        self.y_cord += y_cord
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.image.get_width(), self.image.get_height())

    def draw(self, screem):  # funkcja rysujaca wroga
        game.screen.blit(self.image, (self.x_cord, self.y_cord))
