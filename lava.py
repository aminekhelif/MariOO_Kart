import pygame
import os
import glob
from area import Area


class Lava(Area):
    def __init__(self, x, y):
        Area.__init__(self, x, y)
        self.frame_paths = []  # Store paths instead of loaded images
        self.frames = []
        self.current_frame = 0
        self.last_update_time = 0
        self.frame_delay = 100
        self.initialized = False  # Flag to check if images are converted
        self.load_frame_paths()

    def load_frame_paths(self):
        current_path = os.path.dirname(__file__)
        frames_path = os.path.join(current_path, 'ressources', 'lava', "frame_*_delay-0.1s.png")

        self.frame_paths = sorted(glob.glob(frames_path))
        if not self.frame_paths:
            print("No frame paths found.")
        else:
            pass

    def convert_frames(self):
        for path in self.frame_paths:
            try:
                image = pygame.image.load(path).convert_alpha()
                self.frames.append(image)
            except Exception as e:
                print(f"Error converting image {path}: {e}")
        self.initialized = True

    def draw(self, screen):
        if not self.initialized:
            self.convert_frames()  # Convert images when draw is first called

        now = pygame.time.get_ticks()
        if now - self.last_update_time > self.frame_delay:
            self.last_update_time = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)

        if self.frames:
            screen.blit(self.frames[self.current_frame], (self.x, self.y))
