from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import math

W_Width, W_Height = 500, 500
ballx, bally = 0,0
l = []
speed = 0.1
size = 6
size_f = 0
f = 0
move_f = 0

def draw_points(l):
    glPointSize(size)
    for i in l:
        glColor3f(i[1][0], i[1][1], i[1][2])
        glBegin(GL_POINTS)
        glVertex2f(i[0][0],i[0][1])
        glEnd()

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return [a,b]

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    draw_points(l)

    glutSwapBuffers()

def mouseListener(button, state, x, y):
    global l, size_f, move_f
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            size_f = 1

    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            move_f = 1
            rgb = []
            for i in range(3):
                rgb.append(random.randint(0,255)/255)
            d = random.randint(1,4)
            print(convert_coordinate(x, y))
            l.append([convert_coordinate(x,y),rgb,d])

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed, move_f
    if key==GLUT_KEY_UP:
        if speed == 0:
            move_f = 1
            speed = 0.01
        speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:
        if speed == 0:
            move_f = 1
            speed = 0.01
        speed /= 2
        print("Speed Decreased")

    glutPostRedisplay()

def keyboardListener(key, x, y):
    global speed, move_f, size_f
    if key==b' ':
        size_f = 0
        move_f = 0
        speed = 0

    glutPostRedisplay()

def animate():
    glutPostRedisplay()
    global l, speed, size_f, f, size, move_f
    if move_f == 1:
        for i in range(0,len(l)):
            d = l[i][2]
            if d == 1:
                if l[i][0][0] <= 250 and l[i][0][1] <= 250:
                    l[i][0][0] = (l[i][0][0]+speed)
                    l[i][0][1] = (l[i][0][1]+speed)
                else:
                    if l[i][0][1] > 250 and l[i][0][0] > 0:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][0] > 250 and l[i][0][1] > 0:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
                    elif l[i][0][0] < 0:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][1] < 0:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
            elif d == 2:
                if l[i][0][0] >= -250 and l[i][0][1] <= 250:
                    l[i][0][0] = (l[i][0][0] - speed)
                    l[i][0][1] = (l[i][0][1] + speed)
                else:
                    if l[i][0][1] > 0 and l[i][0][0] < -250:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
                    elif l[i][0][0] < 0 and l[i][0][1] > 250:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][0] > 0:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][1] < 0:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
            elif d == 3:
                if l[i][0][0] >= -250 and l[i][0][1] >= -250:
                    l[i][0][0] = (l[i][0][0] - speed)
                    l[i][0][1] = (l[i][0][1] - speed)
                else:
                    if l[i][0][1] < 0 and l[i][0][0] < -250:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
                    elif l[i][0][0] < 0 and l[i][0][1] < -250:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][0] < 0:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
                    elif l[i][0][1] < 0:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
            elif d == 4:
                if l[i][0][0] <= 250 and l[i][0][1] >= -250:
                    l[i][0][0] = (l[i][0][0] + speed)
                    l[i][0][1]= (l[i][0][1] - speed)
                else:
                    if l[i][0][1] < 0 and l[i][0][0] > 250:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])
                    elif l[i][0][0] > 0 and l[i][0][1] < -250:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][0] < 0:
                        l[i][0][0] = (l[i][0][0])
                        l[i][0][1] = -(l[i][0][1])
                    elif l[i][0][1] > 0:
                        l[i][0][0] = -(l[i][0][0])
                        l[i][0][1] = (l[i][0][1])

    if size_f == 1:
        if size == 0.25:
            f = 1
        elif size == 6:
            f = 0
        if f == 0:
            size -= 0.25
        else:
            size += 0.25


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()