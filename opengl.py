# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# %% [markdown]
# <img src="./cube.png"/>

# %%
cubeVertices = (
    (1,1,1),
    (1,1,-1),
    (1,-1,-1),
    (1,-1,1),
    (-1,1,1),
    (-1,-1,-1),
    (-1,-1,1),
    (-1, 1,-1)
)

triangleVertices = (
    (1, 0, 1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 0, -1)
)

triangleEdges = (
    (0,1),
    (0,2),
    (0,3),
    (1,2),
    (1,2),
    (1,3),
    (1,3),
    (2,3)
)

cubeEdges = (
    (0,1),
    (0,3),
    (0,4),
    (1,2),
    (1,7),
    (2,5),
    (2,3),
    (3,6),
    (4,6),
    (4,7),
    (5,6),
    (5,7)
)

# %%
def triangle():
    glBegin(GL_LINES)

    for edge in triangleEdges:
        for vertex in edge:
            glVertex3fv(triangleVertices[vertex])
    glEnd()

# %%
def cube():
    glBegin(GL_LINES)

    for edge in cubeEdges:
        for vertex in edge:
            glVertex3fv(cubeVertices[vertex])
    glEnd()


# %%
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, -0.5, -10)

    glRotatef(1, 2, 1, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()

