import pygame
import random

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

class Ball:
    def __init__(self, color, pos, radius):
        self.color = color
        self.pos = list(pos)
        self.radius = radius
        self.velocity = [random.randint(50, 100), 0]
        self.activate = False
        self.restitution = 1

    def move(self, dt):
        self.pos[0] += self.velocity[0] * dt  # Update position based on velocity

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def gravity(self, dt):
        acceleration = [0, 100]

        self.velocity[1] += acceleration[1] * dt  # Update velocity
        self.pos[1] += self.velocity[1] * dt  # Update position based on velocity

    def wall_collision_check(self, dt):
        # Check if ball has hit the ground
        if self.pos[1] > height - self.radius:
            self.pos[1] = height - self.radius  # Reset position to ground level
            self.velocity[1] = -self.velocity[1] * self.restitution

        # Check if ball has hit the sides and rebound
        if self.pos[0] > width - self.radius:
            self.pos[0] = width - self.radius
            self.velocity[0] = -self.velocity[0]
        elif self.pos[0] < 0 + self.radius:
            self.pos[0] = 0 + self.radius
            self.velocity[0] = -self.velocity[0]

        if self.pos[1] < 0 + self.radius:
            self.pos[1] = 0 + self.radius
            self.velocity[1] = -self.velocity[1]

num_of_balls = 100
balls = []

for ball in range(num_of_balls):
    color = random.randint(20, 255), 0, random.randint(20, 255)
    radius = 1
    pos = random.randint(0, width - radius), random.randint(0, height - radius)
    balls.append(Ball(color, pos, radius))

def CollisionDetection(balls):
    for i in range(len(balls)):
        current_ball = balls[i]

        if i + 1 < len(balls):
            next_ball = balls[i + 1]
#            print("next", next_ball.pos)  # Ensure this prints the correct next ball position
#            print("current", current_ball.pos)  # Ensure this prints the correct current ball position

            if not ((abs(current_ball.pos[0] - next_ball.pos[0]) >= current_ball.radius + next_ball.radius) or \
                    (abs(current_ball.pos[1] - next_ball.pos[1]) >= current_ball.radius + next_ball.radius)):
                print("COLLISION")

run = True
while run:
    dt = clock.tick(30) / 1000.0
    screen.fill((0, 0, 0))

    for ball in balls:
        ball.draw(screen)
        ball.move(dt)
        ball.wall_collision_check(dt)

    CollisionDetection(balls)

    key = pygame.key.get_pressed()

    if key[pygame.K_f]:
        for ball in balls:
            if not ball.activate:
                ball.activate = True

    for ball in balls:
        if ball.activate:
            ball.gravity(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

