import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Particle Art")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = (random.randint(0, 255), 
                     random.randint(0, 255), 
                     random.randint(0, 255))
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)
        self.life = random.randint(50, 150)

    def update(self, mouse_x, mouse_y):
        # Move towards mouse with some randomness
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 5:
            self.angle = math.atan2(dy, dx) + random.uniform(-0.2, 0.2)
            self.x += math.cos(self.angle) * self.speed
            self.y += math.sin(self.angle) * self.speed
        
        self.life -= 1

    def draw(self):
        if self.life > 0:
            alpha = int((self.life / 150) * 255)
            surface = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
            pygame.draw.circle(surface, (*self.color, alpha), 
                             (self.size, self.size), self.size)
            screen.blit(surface, (int(self.x)-self.size, int(self.y)-self.size))

# Particle list
particles = []

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add more particles on click
            for _ in range(10):
                particles.append(Particle(event.pos[0], event.pos[1]))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Add new particles randomly
    if random.random() < 0.3:
        particles.append(Particle(random.randint(0, WIDTH), 
                                random.randint(0, HEIGHT)))

    # Update and draw
    screen.fill(BLACK)
    
    # Update particles
    for particle in particles[:]:
        particle.update(mouse_x, mouse_y)
        particle.draw()
        if particle.life <= 0:
            particles.remove(particle)

    # Draw mouse attraction point
    pygame.draw.circle(screen, WHITE, (mouse_x, mouse_y), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
