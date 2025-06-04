import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# initialize pygame and openGL
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cube Flight')

# perspective
gluPerspective(45, (width/height), 0.1, 1000.0)
# move camera back a bit
glTranslatef(0.0, 0.0, -50)

def draw_cube():
    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        for vertex in surface:
            glVertex3fv(cube_vertices[vertex])
    glEnd()

def draw_scene(player_pos):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # draw stars
    for s in stars:
        glPushMatrix()
        glTranslatef(s[0], s[1], s[2])
        glScalef(0.3, 0.3, 0.3)
        draw_cube()
        glPopMatrix()

    # draw player cube
    glPushMatrix()
    glTranslatef(*player_pos)
    draw_cube()
    glPopMatrix()

    pygame.display.flip()

cube_vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

cube_surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

# generate stars at random positions
star_count = 100
star_range = 100
stars = [(random.uniform(-star_range, star_range),
          random.uniform(-star_range, star_range),
          random.uniform(-star_range, star_range-50))
         for _ in range(star_count)]

player_pos = [0.0, 0.0, -20.0]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 0.5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 0.5
    if keys[pygame.K_UP]:
        player_pos[1] += 0.5
    if keys[pygame.K_DOWN]:
        player_pos[1] -= 0.5
    if keys[pygame.K_w]:
        player_pos[2] += 0.5
    if keys[pygame.K_s]:
        player_pos[2] -= 0.5

    draw_scene(player_pos)
    clock.tick(60)
