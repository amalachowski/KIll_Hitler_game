import pygame


class Button:
    def __init__(self, x_cord, y_cord, file_name):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_image = pygame.image.load(f"{file_name}.png")
        self.hovered_button_image = pygame.image.load(f"{file_name}_how.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(),
                                  self.button_image.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw_button_play(self, screen):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.hovered_button_image, (self.x_cord, self.y_cord))
        else:
            screen.blit(self.button_image, (self.x_cord, self.y_cord))
