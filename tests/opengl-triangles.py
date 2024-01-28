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
    [(0, 0, 0),(0,0)]
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
n = 0
r = 1


def Painter(edges, vertices):
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex][0])
    glEnd()


def Morpher():
    global a,b,c,d,e,f,n,r
    for vertex in vertices:
        x,y,z = vertex[0]
        a,b = vertex[1]

        if (x,y) != (0,0):
            for vertex1 in vertices:
                xv1, yv1, zv1 = vertex1[0]
                if distanceCalc((xv1,yv1,0), vertex1[0]) >= 1:
                    newPoint(xv1, yv1, 0)
            vertices.remove(vertex)

            x += a
            y += b

            vtex = [(x,y,0),(a,b)]
            vertices.append(vtex)

def distanceCalc(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def rootPoint(x=0,y=0,z=0):
    vertices.append((x,y,z))

def newPoint(x,y,z):
    a = random.randint(-1,1)*random.random()
    b = random.randint(-1,1)*random.random()
    x += random.random()
    y += random.random()
    vertices.append([(x,y,0), (a,b)])
    

def main():
    pygame.init()

    FPS=10
    fpsClock=pygame.time.Clock()

    display = (1920, 1080)
    pygame.display.set_mode(display,pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("main")
    gluPerspective(45, (display[0]/display[1]), 10, 10000.0)
    glTranslatef(0,0, -20)

    newPoint(0.001,0.001,0)

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

        Painter(edges,vertices)
        Morpher()
        pygame.display.flip()
        fpsClock.tick(FPS)

        
        




main()