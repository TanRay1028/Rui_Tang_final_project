import pygame, random

class Orange:
    def __init__(self, img_path, screen_width, screen_height):
        self.orange = self.load_file(img_path)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pos_x = 0
        self.pos_y = 0
        self.orange_spawn()


    @staticmethod
    def load_file(file):
        return pygame.image.load(file).convert_alpha()

    # Randomly spawn the orange
    def orange_spawn(self):
        margin = 200
        self.pos_x = random.randint(200, self.screen_width - self.orange.get_width())
        self.pos_y = random.randint(200, self.screen_height - self.orange.get_height())

    def draw(self, screen):
        screen.blit(self.orange,(self.pos_x, self.pos_y))

    # get the rectangle of orange
    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.orange.get_width(), self.orange.get_height())