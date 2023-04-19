import sys
import random
from PIL import Image
import pygame

# Load the image and get pixel values
image_path = 'C:\\Users\\NIKHIL\\Desktop\d7e64wm-09bd8948-43d7-46cc-9f8f-e5cdc2c7b4ae.png'
img = Image.open(image_path)
width, height = img.size
pixels = list(img.getdata())

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Image Dots Animation')

# Create dot objects with random initial positions
class Dot:
    def __init__(self, x, y, color):
        self.x = random.randint(0, width-1)
        self.y = random.randint(0, height-1)
        self.target_x = x
        self.target_y = y
        self.color = color

    def move(self):
        if self.x < self.target_x:
            self.x += 1
        elif self.x > self.target_x:
            self.x -= 1

        if self.y < self.target_y:
            self.y += 1
        elif self.y > self.target_y:
            self.y -= 1

dots = [Dot(x, y, pixels[y * width + x]) for y in range(height) for x in range(width)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for dot in dots:
        dot.move()
        pygame.draw.circle(screen, dot.color, (dot.x, dot.y), 1)

    pygame.display.flip()

pygame.quit()
sys.exit()
