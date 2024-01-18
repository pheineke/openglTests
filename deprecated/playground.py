import pygame
import math
import time
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

backgroundcolor = (255,255,255)
color0 = (0,0,0)
Pi = 3.14

timeinterval = 1


#### OPENGL

'''
vertices = (
    (1, -1, -5),
    (1, 1, -5),
    (-1, 1, -1),
    (-1, 5, -1),
    (1, -1, 5),
    (1, 1, 5),
    (-1, -1, 1),
    (-1, 5, 1)
    )



edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (0,0,0),
    (0,0,0),
    (0,50,0),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )
'''




def Cube(edges, vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()

    FPS=30
    fpsClock=pygame.time.Clock()

    display = (1920, 1080)
    pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
    pygame.display.set_caption("main")
    gluPerspective(45, (display[0]/display[1]), 10, 100.0)
    glTranslatef(0,0, -20)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        
        events = pygame.key.get_pressed()
        if events[pygame.K_UP]:
            glRotatef(5,0,1,0)
        if events[pygame.K_DOWN]:
            glRotatef(5,0,-1,0)
        if events[pygame.K_LEFT]:
            glRotatef(5,1,0,0)
        if events[pygame.K_RIGHT]:
            glRotatef(5,-1,0,0)
        if events[pygame.K_w]:
            glTranslatef(0,0.5,0)
        if events[pygame.K_s]:
            glTranslatef(0,-0.5,0)
        if events[pygame.K_a]:
            glTranslatef(-0.5,0,0)
        if events[pygame.K_d]:  
            glTranslatef(0.5,0,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0,0,1.0)
            if event.button == 5:
                glTranslatef(0,0,-1.0)
            
            
            
        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube(edges,vertices)
        Cube(edges,vertices)
        pygame.display.flip()
        fpsClock.tick(FPS)

        
        




main()


###########
