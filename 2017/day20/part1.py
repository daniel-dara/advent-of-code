import re
from itertools import islice
from math import sqrt
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int
    z: int

    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)


class Particle(NamedTuple):
    id: int
    position: Vector
    velocity: Vector
    acceleration: Vector


particles = []

# take all minimum acceleration (abs)
# take acceleration opposite of velocity
# take smallest initial velocity
for index, line in enumerate(open('input.txt')):
    values = map(int, re.findall('-?\\d+', line))
    particles.append(Particle(index, *(Vector(x, y, z) for x, y, z in (islice(values, 3) for i in range(3)))))

# Thankfully there are no ties to break for minimum acceleration, otherwise initial velocity and positions would have
# to be accounted for.
print('part 1:', min(particles, key=lambda x: x.acceleration.magnitude()).id)

