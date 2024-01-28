import random
import pygame
import math
import time
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import colorsys

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

colors = [

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
n = 0
r = 1


def Cube(edges, vertices):
    glBegin(GL_LINES)
    a = 1.0
    b = 0.1
    counter = 0
    for edge in edges:
        for vertex in edge:
            
            f = colorsys.hsv_to_rgb(a,b,1)
            colors.append(f)
            ag, ba, ca = colors[counter][0], colors[counter][1], colors[counter][2]
            glColor3f(ag,ba,ca)
            
            glVertex3fv(vertices[vertex])


            counter +=1
            a -= 0.005
            b += 0.02
            
    glEnd()


def Morpher():
    global a,b,c,d,e,f,n,r
    x, y, z = vertices[len(vertices)-1]

    if f == 0:
        if n == 0:
            x += r
            n += 1

        elif n == 1:
            y += r
            n += 1
            
        else:
            z += r
            n = 0
            f = 1
            r += 1

    else:
        if n == 0:
            x -= r
            n += 1

        elif n == 1:
            y -= r
            n += 1
        
        else:
            z -= r
            n = 0
            f = 0
            r += 1

    v0 = x, y, z
    vertices.append(v0)

    vertlen = len(vertices)
    edges.append((vertlen-1,vertlen-2))



def main():
    pygame.init()

    FPS=10
    fpsClock=pygame.time.Clock()

    display = (1920, 1080)
    pygame.display.set_mode(display,pygame.DOUBLEBUF | pygame.OPENGL | pygame.NOFRAME)
    pygame.display.set_caption("main")
    gluPerspective(45, (display[0]/display[1]), 2, 10000.0)
    glTranslatef(0,0, -20)

    run = 0
    rg, bz, ra = 1,1,1

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
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 3, 1, 1)
        Cube(edges,vertices)

        
        glColor3f(rg, bz, ra)

        rg = random.random()
        bz = random.random()
        ra = random.random()
        if run < 1000:
            print(run)
            
            
            #Cube(edges,vertices)
            
            Morpher()
        
            run +=1
        pygame.display.flip()
        fpsClock.tick(FPS)



main()