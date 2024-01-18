from numpy import sin, cos, radians

import pickle
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import compileProgram, compileShader

from PIL import Image

##### LOCAL
import movement
import worldgenerator
from camera import Camera

camera_x, camera_y, camera_z = 0, 0, 0
camera_angle_x, camera_angle_y = 0, 0


cam = Camera()
WIDTH, HEIGHT = 1280, 720
display = (WIDTH, HEIGHT)
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True



def mouse_look(xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)



def draw_edges_and_vertices(pixel_matrix):
    points = []

    glBegin(GL_LINES)  # Beginnen mit dem Zeichnen von Linien

    bla = 60.0

    for y, row in enumerate(pixel_matrix[:-1]):  # Das letzte Element in der Zeile wird übersprungen
        for x, pixel_value in enumerate(row[:-1]):  # Das letzte Element in der Spalte wird übersprungen
            gray_value = pixel_value / bla

            # Punkte verbinden: (x, y) mit (x+1, y), (x, y) mit (x, y+1), und (x, y) mit (x+1, y+1)
            glColor3f(gray_value, gray_value, gray_value)
            glVertex3f(x, y, gray_value)
            glVertex3f(x + 1, y, pixel_matrix[y][x + 1] / bla)

            glVertex3f(x, y, gray_value)
            glVertex3f(x, y + 1, pixel_matrix[y + 1][x] / bla)

            glVertex3f(x, y, gray_value)
            glVertex3f(x + 1, y + 1, pixel_matrix[y + 1][x + 1] / bla)

    glEnd()




def main(pixelmatrix):
    pygame.init()

    pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE) # |pygame.FULLSCREEN
    #pygame.mouse.set_visible(True)
    pygame.event.set_grab(True)



    gluPerspective(90, (display[0]/display[1]), 0.1, 1000.0)

    glTranslatef(0.0,0.0, -1)

    fpsClock = pygame.time.Clock()
    
    fpsList = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                print(sum(fpsList) / len(fpsList))
                pygame.quit()
                quit()
        
        movement.handle_camera_movement()

        glTranslatef(-camera_x, -camera_y, -camera_z)
        glRotatef(-camera_angle_x,1,0,0)
        glRotatef(-camera_angle_y,0,1,0)

        #glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        draw_edges_and_vertices(pixelmatrix)

        pygame.display.flip()

        fps = fpsClock.tick()
        fpsList.append(fps)




pixelmatrix = worldgenerator.worldgenerator("./heightmaps/", "heightmap3", "heightmap3")
main(pixelmatrix)
