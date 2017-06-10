import Particles
import Window
import sys
import random


def find_particle(particles, x, y):
    for particle in particles:
        if Particles.math.hypot(particle.x - x, particle.y - y) <= particle.size:
            return particle
    return None


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    distance = Particles.math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        tangent = Particles.math.atan2(dy, dx)
        p1.angle = 2 * tangent - p1.angle
        p2.angle = 2 * tangent - p2.angle
        (p1.speed, p2.speed) = (p2.speed, p1.speed)
        p1.speed *= p1.elasticity
        p2.speed *= p2.elasticity
        angle = 0.5 * Particles.math.pi + tangent
        p1.x += Particles.math.sin(angle)
        p1.y -= Particles.math.cos(angle)
        p2.x -= Particles.math.sin(angle)
        p2.y += Particles.math.cos(angle)


def main():
    particles = []
    window = Window.Window()
    for n in range(30):
        size = random.randint(10, 20)
        x = random.randint(size, window.width - size)
        y = random.randint(size, window.height - size)
        new_particle = Particles.Particle((x, y), size, window)
        new_particle.speed = random.random()
        new_particle.angle = random.uniform(0, Particles.math.pi * 2)
        particles.append(new_particle)
    selected_particle = None
    sx = 0
    sy = 0
    k = 0.1
    while 1:
        for event in Window.pygame.event.get():
            if event.type == Window.pygame.QUIT:
                sys.exit()
            elif event.type == Window.pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = Window.pygame.mouse.get_pos()
                selected_particle = find_particle(particles, mouseX, mouseY)
                if selected_particle:
                    sx = selected_particle.x
                    sy = selected_particle.y
                    k = 0.1
            elif event.type == Window.pygame.MOUSEBUTTONUP:
                selected_particle = None

        if selected_particle:
            k += 0.03
            (mouseX, mouseY) = Window.pygame.mouse.get_pos()
            dx = mouseX - sx
            dy = mouseY - sy
            selected_particle.angle = Particles.math.atan2(dy, dx) + 0.5 * Particles.math.pi
            selected_particle.speed = Particles.math.hypot(dx, dy) * 0.01 / k
            selected_particle.display()
            selected_particle.x = mouseX
            selected_particle.y = mouseY
        window.fill()
        for i, particle in enumerate(particles):
            particle.move()
            particle.bounce()
            for particle2 in particles[i + 1:]:
                collide(particle, particle2)
            particle.display()
        Window.pygame.display.flip()


if __name__ == '__main__':
    main()
