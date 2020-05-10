from __future__ import annotations

import itertools
import re
from collections import defaultdict
from itertools import islice
from math import sqrt
from typing import NamedTuple, Dict, Set, Optional


class Vector(NamedTuple):
    x: int
    y: int
    z: int

    def distance(self, other: Vector) -> float:
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)

    def magnitude(self) -> float:
        return self.distance(Vector(0, 0, 0))

    def add(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


class Particle(NamedTuple):
    id: int
    position: Vector
    velocity: Vector
    acceleration: Vector

    @staticmethod
    def collide(particle_a: Particle, particle_b: Particle) -> Optional[Collision]:
        tick = 0

        while True:
            distance = particle_a.distance(particle_b)

            if distance == 0:
                return Collision(tick, particle_a.position, {particle_a, particle_b})

            particle_a = particle_a.tick()
            particle_b = particle_b.tick()
            tick += 1

            if particle_a.distance(particle_b) > distance:
                return None

    def tick(self) -> Particle:
        new_velocity = self.velocity.add(self.acceleration)
        new_position = self.position.add(new_velocity)
        return Particle(self.id, new_position, new_velocity, self.acceleration)

    def distance(self, other: Particle) -> float:
        return self.position.distance(other.position)


class Collision(NamedTuple):
    tick: int
    position: Vector
    particles: Set[Particle]


particles = []


def part1() -> int:
    for index, line in enumerate(open('input.txt')):
        values = map(int, re.findall('-?\\d+', line))
        particles.append(Particle(index, *(Vector(x, y, z) for x, y, z in (islice(values, 3) for _ in range(3)))))

    # Thankfully there were no ties to break for minimum acceleration. If so then initial velocity and positions would
    # have to be considered.
    return min(particles, key=lambda x: x.acceleration.magnitude()).id


def part2():
    # tick to position to colliding particles
    collision_map: Dict[int, Dict[Vector, Set[Particle]]] = defaultdict(lambda: defaultdict(lambda: set()))

    for particle_a, particle_b in itertools.combinations(particles, 2):
        collision = Particle.collide(particle_a, particle_b)

        if collision is not None:
            collision_map[collision.tick][collision.position] |= collision.particles

    collided: Set[Particle] = set()

    for tick, collisions in collision_map.items():
        for position, colliding in collisions.items():
            colliding -= collided

            if len(colliding) >= 2:
                collided |= colliding

    return len(particles) - len(collided)


print('part 1:', part1())
print('part 2:', part2())
