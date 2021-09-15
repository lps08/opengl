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

superficies = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (3, 1, 2),
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (0,1,1),
)


def piramide():
    """
        Função que realiza a construção da pirâmide
    """

    # usando gl_quads pois as cores serão definidas a partir das superficie da pirâmide
    glBegin(GL_QUADS)

    # percorrendo as superficies
    for superfice in superficies:

        # index onde será percorrido a lista de cores já definida
        idx = 0

        # percorrendo cada vertice de uma superficie
        for vertice in superfice:
            # aplicando a cor no index idx
            glColor3fv(colors[idx])
            # passando para o proximo index
            idx += 1

            # criando o triangulo
            glVertex3fv(piramideVertices[vertice])

    glEnd()

    # usando o gl_lines para desenhar as linhas da piramide
    glBegin(GL_LINES)

    # percorrendo cada vertice no ponto de junção para construir a piramide
    for edge in piramideEdges:
        # percorrendo os vertices
        for vertice in edge:
            # desenhando as linhas
            glVertex3fv(piramideVertices[vertice])
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
    gluPerspective(40, (display[0]/display[1]), 0.1, 30.0)

    # adicionanodo a translação
    glTranslatef(0.0, -0.5, -20)

    # rotacionando o objeto inicial
    glRotatef(30, 2, 1, 2)

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

