import pygame
import os


class Cat:
    def __init__(self, frame_folder, screen_width, screen_height):
        self.frames = self.load_frames(frame_folder)
        self.index = 0
        self.counter = 0
        self.delay = 6
        self.pos_x = screen_width - 100
        self.pos_y = screen_height - 100
        self.speed = 5.2

    # load cat_element
    @staticmethod
    def load_frames(folder):
        frames = []
        for i in range(8):
            path = os.path.join(folder, f'frame_{i}.png')
            image = pygame.image.load(path).convert_alpha()
            frames.append(image)
        return frames

    def chase(self, doro_x, doro_y):
        base_speed = self.speed
        dx = doro_x - self.pos_x
        dy = doro_y - self.pos_y
        slower_range = 300

        # calculate the distance
        distance = (dx**2 + dy**2) **0.5

        # if cat catch up doro than quit
        if distance == 0:
            return

        # speed up
        speed = base_speed
        if distance < slower_range:
            speed = base_speed - (slower_range - distance) / 200

        move_x = speed * dx / distance
        move_y = speed * dy / distance
        self.pos_x += move_x
        self.pos_y += move_y

    def update(self):
        self.counter += 1
        if self.counter >= self.delay:
            self.counter = 0
            self.index = (self.index + 1) % len(self.frames)

    def draw(self, screen):
        screen.blit(self.frames[self.index], (self.pos_x, self.pos_y))

    # get the rectangle of orange
    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.frames[0].get_width(), self.frames[0].get_height())