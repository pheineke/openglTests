import random
import pygame
import math
import time
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

rootPoint = [
    (0.0,0.0)
]

singlevertices = [
    (0.0,0.0)
]

edges = [

]

def newPoint(tuple0):
    if not singlevertices.__contains__(tuple0):
        singlevertices.append(tuple0)

def updater():
    i = False
    lastelemRoot = rootPoint[:-1]
    for point0 in singlevertices:
        p0index = singlevertices.index(point0)

        a, b = point0
        a += random.random() * random.randint(-1,1)
        b += random.random() * random.randint(-1,1)
        singlevertices[p0index] = (a,b)

        for point1 in rootPoint:
            p1index = rootPoint.index(point1)

            distance = distanceCalc(point0,point1)
            if distance >= 1 and distance <= 2:
                rootPoint.append(point0)
                index = rootPoint.index(point0)
                edges.append((p1index, index))
        
        


def distanceCalc(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p2[1] - p1[1])**2)


def draw_point():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glColor3f(1.0, 0.5, 1.0)    # Set the color of the point (white in this case)
    glPointSize(2.0)            # Set the size of the point (optional)

    # Begin drawing points
    glBegin(GL_POINTS | GL_LINES)  

    for a,b in rootPoint:
        glVertex2f(a,b)

    for x,y in singlevertices:
        glVertex2f(x,y)


    for edge in edges:
        for vertex in edge:
            glVertex2fv(rootPoint[vertex])
    

    # Coordinates of the point (change as needed)
    


    glEnd()  # End drawing points
    glFlush()  # Ensure that the OpenGL commands are immediately executed

def main():
    pygame.init()

    FPS=2
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
        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        draw_point()
        updater()

        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
