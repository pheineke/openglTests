from numpy import sin, cos, radians

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from PIL import Image


camera_x, camera_y, camera_z = 0, 0, 0
camera_angle_x, camera_angle_y = 0, 0

def heightgrabber():
    img = Image.open('heightmap3.png')
    img_gray = img.convert('L')
    width, height = img_gray.size
    pixel_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = img_gray.getpixel((x, y))
            row.append(pixel_value*10)
        pixel_matrix.append(row)

    return pixel_matrix


def draw_edges_and_vertices():
    points = []
    pixel_matrix = heightgrabber()

    glBegin(GL_LINES)  # Beginnen mit dem Zeichnen von Linien

    for y, row in enumerate(pixel_matrix[:-1]):  # Das letzte Element in der Zeile wird übersprungen
        for x, pixel_value in enumerate(row[:-1]):  # Das letzte Element in der Spalte wird übersprungen
            gray_value = pixel_value / 50.0

            # Punkte verbinden: (x, y) mit (x+1, y), (x, y) mit (x, y+1), und (x, y) mit (x+1, y+1)
            glColor3f(gray_value, gray_value, gray_value)
            glVertex3f(x, y, gray_value)
            glVertex3f(x + 1, y, pixel_matrix[y][x + 1] / 50.0)

            glVertex3f(x, y, gray_value)
            glVertex3f(x, y + 1, pixel_matrix[y + 1][x] / 50.0)

            glVertex3f(x, y, gray_value)
            glVertex3f(x + 1, y + 1, pixel_matrix[y + 1][x + 1] / 50.0)

    glEnd()

def handle_camera_movement():
    speed = 1  # Geschwindigkeit der Kamerabewegung
    rotation_speed = 1  # Geschwindigkeit der Kamerarotation

    keys = pygame.key.get_pressed()

    forward_x = -sin(radians(camera_angle_y))
    forward_z = cos(radians(camera_angle_y))
    right_x = cos(radians(camera_angle_y))
    right_z = sin(radians(camera_angle_y))

    if keys[pygame.K_w]:  # Vorwärtsbewegung in Blickrichtung der Kamera
        glTranslatef(-speed * right_x, +speed * right_z, 0)
        
        #glTranslatef(speed * forward_x, 0, speed * forward_z)
    elif keys[pygame.K_s]:  # Rückwärtsbewegung in Blickrichtung der Kamera
        glTranslatef(+speed * right_x, -speed * right_z, 0)
        #glTranslatef(-speed * forward_x, 0, -speed * forward_z)

    if keys[pygame.K_a]:  # Seitwärtsbewegung nach links relativ zur Blickrichtung der Kamera
        glTranslatef(-speed * right_x, 0, -speed * right_z)
    elif keys[pygame.K_d]:  # Seitwärtsbewegung nach rechts relativ zur Blickrichtung der Kamera
        glTranslatef(speed * right_x, 0, speed * right_z)

    if keys[pygame.K_SPACE]:
        glTranslatef(-speed * forward_x, 0, -speed * forward_z)
    elif keys[pygame.K_LSHIFT]:
        glTranslatef(speed * forward_x, 0, speed * forward_z)

    if keys[pygame.K_UP]:  # Blick nach oben
        glRotatef(rotation_speed, 1, 0, 0)
    elif keys[pygame.K_DOWN]:  # Blick nach unten
        glRotatef(-rotation_speed, 1, 0, 0)

    if keys[pygame.K_LEFT]:  # Blick nach links
        glRotatef(rotation_speed, 0, 1, 0)
    elif keys[pygame.K_RIGHT]:  # Blick nach rechts
        glRotatef(-rotation_speed, 0, 1, 0)





def main():
    pygame.init()
    display = (720,480)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)

    glTranslatef(0.0,0.0, -5)

    fpsClock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        handle_camera_movement()


        glTranslatef(-camera_x, -camera_y, -camera_z)
        glRotatef(-camera_angle_x,1,0,0)
        glRotatef(-camera_angle_y,0,1,0)

        #glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #
        draw_edges_and_vertices()

        pygame.display.flip()


        fps = int(fpsClock.get_fps())

        print(fpsClock.tick())



main()
