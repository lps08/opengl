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

# definindo as superficies
superficies = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (3, 2, 1),
)

# definindo as faces do poligono
normals = [
    ( 0,  0, -1),  
    (-1,  0,  0),  
    ( 1,  0,  0),  
    ( 0,  1,  0),
]

# lista de cores
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
    for i_superficie, superfice in enumerate(superficies):

        # index onde será percorrido a lista de cores já definida
        idx = 0

        # adicionando superficies normais para pegar a luz
        glNormal3fv(normals[i_superficie])

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
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # adicionanodo a translação
    glTranslatef(0.0, 0, -5)

    # glRotatef(-50, 10, -10, 1)
    # parametros de iluminação
    glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0))
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    # loop que faz a renderização do objeto utilizando o pygame
    while True:
        for event in pygame.event.get():
            # se o usuario fechar a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # habilitação da iluminação
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        # glRotatef(1, 3, 1, 1)
        # chamando o objeto criado
        piramide()

        pygame.display.flip()
        pygame.time.wait(10)

# inicializando a função principal
if __name__ == '__main__':
    main()

