import math


class Particle:
    @staticmethod
    def add_vectors((angle1, length1), (angle2, length2)):
        x = math.sin(angle1) * length1 + math.sin(angle2) * length2
        y = math.cos(angle1) * length1 + math.cos(angle2) * length2
        length = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y, x)
        return angle, length

    def __init__(self, (x, y), size, window):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.Window = window
        self.speed = 0.01
        self.angle = math.pi / 2
        self.gravity = (math.pi, 0.002)
        self.drag = 0.999
        self.elasticity = 0.75

    def display(self):
        self.Window.draw(int(self.x), int(self.y), self.size, self.thickness, self.colour)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        (self.angle, self.speed) = self.add_vectors((self.angle, self.speed), self.gravity)
        self.speed *= self.drag

    def bounce(self):
        if self.x > self.Window.width - self.size:
            self.x = 2 * (self.Window.width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
        if self.y > self.Window.height - self.size:
            self.y = 2 * (self.Window.height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
