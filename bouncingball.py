import math

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
        self.mass = 1

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


num_of_balls = 10
balls = []

for ball in range(num_of_balls):
    color = random.randint(20, 255), 0, random.randint(20, 255)
    radius = 10
    pos = random.randint(0, width - radius), random.randint(0, height - radius)
    balls.append(Ball(color, pos, radius))


def CollisionDetection(balls):
    for i in range(len(balls)):
        current_ball = balls[i]

        for j in range(i + 1, len(balls)):
            next_ball = balls[j]

            dx = next_ball.pos[0] - current_ball.pos[0]
            dy = next_ball.pos[1] - current_ball.pos[1]
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance <= current_ball.radius + next_ball.radius:
                print("collision")

                normal_vector = [next_ball.velocity[0] - current_ball.velocity[0],
                                 next_ball.velocity[1] - current_ball.velocity[1]]
                normal_vector_magnitude = math.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)

                unit_normal_vector = [(normal_vector[0] / normal_vector_magnitude),
                                      (normal_vector[1] / normal_vector_magnitude)]
                unit_tangent_vector = [-(normal_vector[1] / normal_vector_magnitude),
                                       (normal_vector[0] / normal_vector_magnitude)]

                # let v1 = ball 1 velocity, v2 = ball 2 velocity, n = normal, t = tangent
                # scalar projection = unit vector b * vector a

                scalar_projection_v1n = dot_product(current_ball.velocity, unit_normal_vector)
                scalar_projection_v1t = dot_product(current_ball.velocity, unit_tangent_vector)
                scalar_projection_v2n = dot_product(next_ball.velocity, unit_normal_vector)
                scalar_projection_v2t = dot_product(next_ball.velocity, unit_tangent_vector)

                # final tangential velocity does not change as the impulse is normal to the surface

                scalar_final_normal_v1 = (scalar_projection_v1n * (current_ball.mass - next_ball.mass)
                                          + 2 * next_ball.mass * scalar_projection_v2n) / (
                                                     current_ball.mass + next_ball.mass)

                scalar_final_normal_v2 = (scalar_projection_v2n * (next_ball.mass - current_ball.mass)
                                          + 2 * current_ball.mass * scalar_projection_v1n) / (
                                                     current_ball.mass + next_ball.mass)

                final_normal_vector_v1 = multiply_vector_by_scalar(scalar_final_normal_v1, unit_normal_vector)
                final_tangent_vector_v1 = multiply_vector_by_scalar(scalar_projection_v1t, unit_tangent_vector)
                final_normal_vector_v2 = multiply_vector_by_scalar(scalar_final_normal_v2, unit_normal_vector)
                final_tangent_vector_v2 = multiply_vector_by_scalar(scalar_projection_v2t, unit_tangent_vector)

                final_v1_vector = add_vectors(final_normal_vector_v1, final_tangent_vector_v1)
                final_v2_vector = add_vectors(final_normal_vector_v2, final_tangent_vector_v2)

                current_ball.velocity = final_v1_vector
                next_ball.velocity = final_v2_vector


def dot_product(vec1, vec2):
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    return result


def add_vectors(vec1, vec2):
    result = []
    for i in range(len(vec1)):
        result.append(vec1[i] + vec2[i])
    return result


def multiply_vector_by_scalar(scalar, vec):
    result = [0, 0]
    for i in range(len(vec)):
        result[i] = vec[i] * scalar
    return result


run = True
while run:
    dt = clock.tick(60) / 1000.0
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
