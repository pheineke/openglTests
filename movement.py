from numpy import sin, cos, radians

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera

cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True


camera_x, camera_y, camera_z = 0, 0, 0
camera_angle_x, camera_angle_y = 0, 0


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
        glTranslatef(speed * right_x, 0, speed * right_z)
    elif keys[pygame.K_d]:  # Seitwärtsbewegung nach rechts relativ zur Blickrichtung der Kamera
        glTranslatef(-speed * right_x, 0, -speed * right_z)

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

    '''