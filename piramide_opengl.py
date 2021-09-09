import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# definindo as vértices do triangulo
piramideVertices = (
    (0, 0, 1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 0, -1)
)

# definindo cada junção das vértices do triangulo
piramideEdges = (
    (0,1),
    (0,2),
    (0,3),
    (1,2),
    (1,2),
    (1,3),
    (1,3),
    (2,3)
)

def piramide():
    """
        Função que realiza a construção da pirâmide
    """
    glBegin(GL_LINES)

    # percorrendo cada junção para construir a piramide
    for edge in piramideEdges:
        for vertex in edge:
            # desenhando as linhas
            glVertex3fv(piramideVertices[vertex])
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

    # adicionanodo a translação
    glTranslatef(0.0, -0.5, -10)

    # rotacionando o objeto inicial
    glRotatef(1, 2, 1, 2)

    # usando a escala no objeto
    glScale(4, 4, 4)

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
        piramide()

        pygame.display.flip()
        pygame.time.wait(10)

# inicializando a função principal
if __name__ == '__main__':
    main()

