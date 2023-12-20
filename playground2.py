import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (

    #Mittelbau-Top:
    (-0.25,-0.25,2),    #   0
    (-0.25,0,2),        #   1
    (-0.25,0.25,2),     #   2

    (0,-0.25,1),        #   3
    (0,0,1),            #   4
    (0,0.25,1),         #   5

    (0,-0.25,0),        #   6
    (0,0,0),            #   7
    (0,0.25,0),         #   8

    (0,-0.25,-1),       #   9
    (0,0,-1),           #   10
    (0,0.25,-1),        #   11

    (0,-0.25,-2.5),     #   12
    (0,0,-2.5),         #   13
    (0,0.25,-2.5),      #   14

    #Mittelbau-Seiten
    (-0.25,-0.5,1),     #   15
    (-0.25,0.5,1),      #   16

    (-0.25,-0.5,0),     #   17

    (-0.25,-0.5,0),     #   18


    (-0.25,-0.5,-1),    #   19

    (-0.25,0.5,-1),     #   20

    (-0.25,-0.5,-2),    #   21
    (-0.25,0.5,-2),     #   22

    )

edges = (

    #Mittelbau-Quer-Top
    (0,1),(1,2),

    (3,4),(4,5),

    (6,7),(7,8),

    (9,10),(10,11),

    (12,13),(13,14),

    #Mittelbau-Querverbund-Top
    (0,3),(1,4),(2,5),

    (3,6),(4,7),(5,8),

    (6,9),(7,10),(8,11),

    (9,12),(10,13),(11,14),


    #Seiten-Verbund
    (15,17),(17,19),

    #Mittelbau-Seiten-Verbund mit Mittelbau
    (15,3), (16,5),



)


def coords():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def shuttle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()



def main():
    pygame.init()
    display = (1920,1080)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        coords()
        shuttle()
        pygame.display.flip()
        FPS=20
        fpsClock=pygame.time.Clock()
        fpsClock.tick(FPS)


main()
