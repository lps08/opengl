import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# definindo as vértices do triangulo
triangleVertices = (
    (0, 0, 1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 0, -1)
)

# definindo cada junção das vértices do triangulo
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

# definindo as vertices do cubo
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

# Definindo cada junção das vértices do triangulo
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

def triangle():
    """
        Função que realiza a construção da pirâmide
    """
    glBegin(GL_LINES)

    # percorrendo cada junção para construir a piramide
    for edge in triangleEdges:
        for vertex in edge:
            # desenhando as linhas
            glVertex3fv(triangleVertices[vertex])
    glEnd()


def cube():
    """
        Função que realiza a construção de um cubo
    """
    glBegin(GL_LINES)

    # percorrendo cada junção para construir o cubo
    for edge in cubeEdges:
        for vertex in edge:
            # desenhando as linhas
            glVertex3fv(cubeVertices[vertex])
    glEnd()


def main():
    """
        Função principal onde irá renderizar a construção do objeto
    """
    # iniciando o pygame, onde é o responsável pela renderização
    pygame.init()

    # definindo o tamanho do display da janaela de visualização
    display = (800, 600)
    # aplicando o tamanho da tela e definindo as configurações necessárias do opengl
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # adicionando a perspectiva 
    gluPerspective(35, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, -0.5, -10)

    # rotacionando o objeto inicial
    glRotatef(1, 2, 1, 2)

    # loop que faz a renderização do objeto utilizando o pygame
    while True:
        for event in pygame.event.get():
            # se o usuario fechar a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # para cada frame, o objeto rataciona
        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # chamando o objeto criado
        triangle()

        pygame.display.flip()
        pygame.time.wait(10)

# inicializando a função principal
if __name__ == '__main__':
    main()

