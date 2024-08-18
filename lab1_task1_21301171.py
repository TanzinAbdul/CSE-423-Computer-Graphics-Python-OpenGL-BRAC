from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import math

W_Width, W_Height = 1000,1000
l1 = []
l2 = []
speed = 0.5
color_value = 1.0
color_change_rate = 0.05
rain_angle = 0.1
c = 0
ini = []

for i in range(-255,255,5):
    temp = random.randint(240, 250)
    l1.append([i,255])
    l2.append([i,temp])

p = 0
while l1[-1][1] >= -255:
    q = len(l1)
    for i in range(p,q):
        temp = random.randint(15,20)
        l1.append([l2[i][0],l2[i][1]-10])
        l2.append([l1[-1][0],l1[-1][1]-temp])
        if l1[-1][1] <= -255:
            break
    p = q

def drawShapes():
    glBegin(GL_QUADS)
    glColor3f(color_value, color_value, color_value)
    glVertex2d(-600,600)
    glVertex2d(600,600)
    glVertex2d(600,-600)
    glVertex2d(-600,-600)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.4, 0.0, 0.0)
    glVertex2d(-100, 70)
    glVertex2d(100, 70)
    glVertex2d(0, 150)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.4, 0.2, 0)
    glVertex2d(-80,70)
    glVertex2d(80,70)
    glVertex2d(80,-70)
    glVertex2d(-80,-70)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)
    glVertex2d(-55,5)
    glVertex2d(-20,5)
    glVertex2d(-20,-70)
    glVertex2d(-55,-70)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)
    glVertex2d(20, 10)
    glVertex2d(50, 10)
    glVertex2d(50, 40)
    glVertex2d(20, 40)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2d(35, 10)
    glVertex2d(35, 40)
    glVertex2d(50, 25)
    glVertex2d(20, 25)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(-25, -37)
    glEnd()

def rain(l1,l2):
    glColor3f(0, 1, 1)
    glPointSize(3)
    for i in range(0,len(l1)):
      x1,y1 = l1[i]
      x2,y2 = l2[i]
      glLineWidth(1)
      glBegin(GL_LINES)
      glVertex2f(x1, y1)
      glVertex2f(x2, y2)
      glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    drawShapes()
    rain(l1,l2)
    glutSwapBuffers()

def animate():
    global c
    glutPostRedisplay()
    for i in range(0,len(l1)):
        if l2[i][1] >= -255:
            l1[i][1] = (l1[i][1] - speed)
            l2[i][1] = (l2[i][1] - speed)
        else:
            d = abs(l1[i][1] - l2[i][1])
            l1[i][1] = 255
            l2[i][1] = 255 - d

def specialKeyListener(key, x, y):
    global speed, rain_angle,c, ini
    if key==GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:
        speed /= 2
        print("Speed Decreased")
    if key == GLUT_KEY_RIGHT:
        c += 1
        ini = [[],[]]
        for i in range(len(l2)):
            l2[i][0] += rain_angle

    if key == GLUT_KEY_LEFT:
        c -= 1
        for i in range(len(l2)):
            l2[i][0] -= rain_angle
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global color_value, color_change_rate
    if key == b'd':
        if color_value <= 1:
            color_value += color_change_rate
    if key == b'n':
        if color_value >=-1:
            color_value -= color_change_rate

    glutPostRedisplay()

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

glutMainLoop()
