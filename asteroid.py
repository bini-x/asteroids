import pygame, random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_asteroid = self.velocity.rotate(random_angle)
        second_asteroid = self.velocity.rotate(random_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        a1, a2 = (
            Asteroid(self.position.x, self.position.y, new_asteroid_radius),
            Asteroid(self.position.x, self.position.y, new_asteroid_radius),
        )
        a1.velocity = new_asteroid * 1.2
        a2.velocity = second_asteroid * 1.2
