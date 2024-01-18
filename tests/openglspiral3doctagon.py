import random
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

vertices = [
    (0, 0, 0),
]


edges = [
]

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
m = 1
n = 1
r = 1
zähler2 = 0

def Cube(edges, vertices):
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Morpher():
    x, y, z = vertices[len(vertices)-1]
    global f
    global zähler2
    global m
    global n

#|
    if f == 0:
        f = 1
        zähler2 += 1
        m = 1
        x = x + (zähler2)

    #/
    elif f == 1:
        f = 2
        x = x + (zähler2)
        y = y + (zähler2)
        z = z + (zähler2)

    #-
    elif f == 2:
        f = 3
        zähler2 += 1
        y = y + (zähler2)

    #\
    elif f == 3:
        f = 4
        x = x - (zähler2)
        y = y + (zähler2)
        z = z + (zähler2)

    #|
    elif f == 4:
        f = 5
        zähler2 += 1
        x = x - (zähler2)
    
    #/
    elif f == 5:
        f = 6
        x = x - (zähler2)
        y = y - (zähler2)
        z = z - (zähler2)

    #-
    elif f == 6:
        f = 7
        zähler2 += 1
        y = y - (zähler2)

    #\
    else:
        f = 0
        x = x + (zähler2)
        y = y - (zähler2)
        z = z - (zähler2)





    v0 = x, y, z
    vertices.append(v0)

    vertlen = len(vertices)
    edges.append((vertlen-1,vertlen-2))



def main():
    pygame.init()

    FPS=10
    fpsClock=pygame.time.Clock()

    display = (1920, 1080)
    pygame.display.set_mode(display,pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("main")
    gluPerspective(45, (display[0]/display[1]), 10, 10000.0)
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
        if events[pygame.K_SPACE]:
            glTranslatef(0, 0, -1, 0)
        elif events[pygame.K_LSHIFT]:
            glTranslatef(-1, 0, 0, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0,0,1.0)
            if event.button == 5:
                glTranslatef(0,0,-1.0)
            
            
        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube(edges,vertices)
        Cube(edges,vertices)
        Morpher()
        pygame.display.flip()
        fpsClock.tick(FPS)

        
        




main()