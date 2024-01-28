import random
import pygame
import math
import time
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from datetime import datetime

now = datetime.now()
currenttime = now.strftime("%H:%M:%S")

rootPoint = [
    (0.0,1.0),
    (1.0,0.0),
    (-1.0,0.0)
]

edges = [
]

particlestep = 0.2

def motion(velocity=None, direction=None):
    print(str(time))




def distanceCalc(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p2[1] - p1[1])**2)


def draw_point():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glColor3f(1.0, 0.5, 1.0)    # Set the color of the point (white in this case)
    glPointSize(2.0)            # Set the size of the point (optional)

    # Begin drawing points
    glBegin(GL_POINTS)  

    for a,b in rootPoint:
        glVertex2f(a,b)

    
    glEnd()
    glBegin(GL_LINES)

    for edge in edges:
        if edge is not None:
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

        motion()

        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
