# doro.py
import pygame
import os

class Doro:
    def __init__(self, frame_folder, pos=(100, 100)):
        self.frames = self.load_frames(frame_folder)
        self.flipped_frames = self.flip_frame()
        self.index = 0
        self.counter = 0
        self.delay = 5
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = 5.5
        self.facing_right = False

    # load doro_element
    @staticmethod
    def load_frames(folder):
        frames = []
        for i in range(6):
            path = os.path.join(folder, f'frame_{i}.png')
            image = pygame.image.load(path).convert_alpha()
            frames.append(image)
        return frames

    # get a flipped doro
    def flip_frame(self):
        flipped_frames = []
        for frame in self.frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            flipped_frames.append(flipped_frame)
        return  flipped_frames

    # monitor keyboard to change the pos of doro
    def move(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos_x -= self.speed
            self.pos_x = max(0, self.pos_x)
            self.facing_right = False
        elif keys[pygame.K_RIGHT]:
            max_x = screen_width - self.frames[0].get_width()
            self.pos_x  += self.speed
            self.pos_x = min(self.pos_x, max_x)
            self.facing_right = True
        if keys[pygame.K_UP]:
            self.pos_y -= self.speed
            self.pos_y = max(0, self.pos_y)
        elif keys[pygame.K_DOWN]:
            max_y = screen_height - self.frames[0].get_height()
            self.pos_y += self.speed
            self.pos_y = min(max_y, self.pos_y)

    # update the doro_frame
    def update(self):
        self.counter += 1
        if self.counter >= self.delay:
            self.counter = 0
            self.index = (self.index + 1) % len(self.frames)

    # check the doro status and draw her on the screen
    def draw(self, screen):
        if self.facing_right:
            frame = self.flipped_frames[self.index]
        else:
            frame = self.frames[self.index]
        screen.blit(frame, (self.pos_x, self.pos_y))

    # get the rectangle of doro
    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.frames[0].get_width(), self.frames[0].get_height())