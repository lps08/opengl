import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
    (3, 2, 1),
)

normals = [
    ( 0,  0, -1),  # surface 0
    (-1,  0,  0),  # surface 1
    ( 1,  0,  0),  # surface 2
    ( 0,  1,  0)   # surface 5
]

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (0,1,1),
)


def carregarTextura():
    # carregando a imagem para aplicar na superficie do objeto
    textureSurface = pygame.image.load('texture.jpg')
    # transformando a imagem para string, o tipo de que o opengl aceita
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)

    # pegando as dimensionalidade da imegem
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    # habilitando a textura
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    # habilitando os parâmetros a variável que ira receber a textura que irá passar ao objeto
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def piramide():
    glBegin(GL_QUADS)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 0, 1)
    
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(0, 0, 1)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(1, 1, -1)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(0, 0, 1)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1, 0, -1)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1, 1, -1)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(1, 1, -1)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1, 0, -1)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(1, -1, -1)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1, 0, -1)

    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, 1, -1)

    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1, 0, -1)

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

    carregarTextura()

    # adicionando a perspectiva 
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # adicionanodo a translação
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0, -5)

    glRotatef(180, 20, -10, 20)

    # glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
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