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
        self.velocity = 0
        self.activate = False
        self.restitution = 1

    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def gravity(self, dt):
        acceleration = 100

        self.velocity += acceleration * dt  # Update velocity
        self.pos[1] += self.velocity * dt  # Update position based on velocity

        # Check if ball has hit the ground
        if self.pos[1] > height - self.radius:
            self.pos[1] = height - self.radius  # Reset position to ground level
            self.velocity = -self.velocity * self.restitution

num_of_balls = 2
balls = []

for ball in range(num_of_balls):
    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    radius = 20
    pos = random.randint(0, width - radius), random.randint(0, height - radius)
    balls.append(Ball(color, pos, radius))

    def CollisionDetection(balls):
        for i in range(len(balls)):
            current_ball = balls[i]

            if i + 1 < len(balls):
                next_ball = balls[i + 1]
                print("next", next_ball.pos)  # Ensure this prints the correct next ball position
                print("current", current_ball.pos)  # Ensure this prints the correct current ball position

                if not ((abs(current_ball.pos[0] - next_ball.pos[0]) >= current_ball.radius + next_ball.radius) or \
                        (abs(current_ball.pos[1] - next_ball.pos[1]) >= current_ball.radius + next_ball.radius)):
                    print("COLLISION")

run = True
while run:
    dt = clock.tick(30) / 1000.0
    screen.fill((0, 0, 0))

    for ball in balls:
        ball.draw(screen)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        ball.move(-5, 0)
    elif key[pygame.K_d]:
        ball.move(5, 0)
    elif key[pygame.K_w]:
        ball.move(0, -5)
    elif key[pygame.K_s]:
        ball.move(0, 5)
    elif key[pygame.K_f]:
        for ball in balls:
            if not ball.activate:
                ball.activate = True

    for ball in balls:
        if ball.activate:
            ball.gravity(dt)

    CollisionDetection(balls)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

