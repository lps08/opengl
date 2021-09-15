import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def loadTexture():
    textureSurface = pygame.image.load('textura.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_3D, texid)
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

    loadTexture()

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