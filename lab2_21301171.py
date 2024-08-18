from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

W_Width, W_Height = 800,800
l = []

def zone_calc(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    if dx >= 0 and dy >= 0:
        if abs(dx) > abs(dy):
            zone = 0
        else:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            zone = 1

    elif dx <= 0 and dy >= 0:
        if abs(dx) < abs(dy):
            x0, y0 = y0, -x0
            x1, y1 = y1, -x1
            zone = 2
        else:
            x0, y0 = -x0, y0
            x1, y1 = -x1, y1
            zone = 3

    elif dx <= 0 and dy <= 0:
        if abs(dx) > abs(dy):
            x0, y0 = -x0, -y0
            x1, y1 = -x1, -y1
            zone = 4
        else:
            x0, y0 = -y0, -x0
            x1, y1 = -y1, -x1
            zone = 5

    elif dx >= 0 and dy <= 0:
        if abs(dx) < abs(dy):
            x0, y0 = -y0, x0
            x1, y1 = -y1, x1
            zone = 6
        else:
            x0, y0 = x0, -y0
            x1, y1 = x1, -y1
            zone = 7

    draw_line(x0, y0, x1, y1, zone)


def draw_line(x0, y0, x1, y1, zone):
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    E = 2 * dy
    NE = 2 * (dy - dx)
    x = x0
    y = y0
    l_points = [[x, y]]
    while x < x1:
        if d <= 0:
            d += E
            x += 1
        else:
            d += NE
            x += 1
            y += 1
        l_points.append([x, y])

    if zone == 1:
        for i in l_points:
            i[0], i[1] = i[1], i[0]
    elif zone == 2:
        for i in l_points:
            i[0], i[1] = -i[1], i[0]
    elif zone == 3:
        for i in l_points:
            i[0], i[1] = -i[0], i[1]
    elif zone == 4:
        for i in l_points:
            i[0], i[1] = -i[0], -i[1]
    elif zone == 5:
        for i in l_points:
            i[0], i[1] = -i[1], -i[0]
    elif zone == 6:
        for i in l_points:
            i[0], i[1] = i[1], -i[0]
    elif zone == 7:
        for i in l_points:
            i[0], i[1] = i[0], -i[1]

    for i in l_points:
        glBegin(GL_POINTS)
        glVertex2f(i[0], i[1])
        glEnd()

def midpoint_circle(c,r):
    d = 1 - r
    x = 0
    y = r
    points = [x,y]
    while x > y:
        if d >= 0:
            x += 1
            y -= 1
            d += d + 2*x - 2*y
        else:
            x_0 += 1
            d += E
        points.append([x_0, y_0])

    for i in points:
        if zone == 1:
            i[0], i[1] = i[1], i[0]
        elif zone == 2:
            i[0], i[1] = -i[1], i[0]
        elif zone == 3:
            i[0] = -i[0]
        elif zone == 4:
            i[0], i[1] = -i[0], -i[1]
        elif zone == 5:
            i[0], i[1] = -i[1], -i[0]
        elif zone == 6:
            i[0], i[1] = i[1], -i[0]
        elif zone == 7:
            i[1] = -i[1]

    glPointSize(2)
    for i in points:
        glBegin(GL_POINTS)
        glVertex2f(i[0], i[1])
        glEnd()

def diamond():
    global col

    if l1[0][1] == 325:
        col = []
        for i in range(3):
            col.append(random.randint(0,255)/255)
    glColor3f(col[0], col[1], col[2])
    for i in range(0,len(l1)):
        x1, y1 = l1[i]
        x2, y2 = l1[(i+1)%4]
        zone_calc(x1, y1, x2, y2)

def diamond_animate():
    global l1, speed, point, flag

    if l1[0][1] > -405 and collission() != True:
        for i in range(0, len(l1)):
            l1[i][1] = (l1[i][1] - speed)
    elif collission():
        point += 1
        print('Score:',point)
        if point % 10 == 0:
            speed += 0.8
        t_x = random.randint(-365, 365)
        l1 = [[t_x, 325], [t_x - 15, 305], [t_x, 285], [t_x + 15, 305]]
    else:
        print('Game Over! Score:',point)
        flag = 0

def bowl():
    if flag == 1:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
    for i in range(0,len(l2)):
        x1, y1 = l2[i]
        x2, y2 = l2[(i+1)%4]
        zone_calc(x1, y1, x2, y2)

def collission():
    if l2[0][0] < l1[2][0]-15 and l2[3][0] > l1[2][0]+15 and int(l1[2][1]) == -382:
        return True

def buttons():
    global flag, p

    #back_button
    glColor3f(0, 1.0, 1.0)
    zone_calc(-380,355,-300,355)
    zone_calc(-345,380,-380,355)
    zone_calc(-345,325,-380,355)

    #pause_button
    glColor3f(1.0, 1.0, 0.0)
    if p == 1:
        zone_calc(-20, 380, -20, 325)
        zone_calc(20, 380, 20, 325)
    else:
        zone_calc(-20, 380, -20, 325)
        zone_calc(-20, 380, 20, 352.5)
        zone_calc(-20, 325, 20, 352.5)

    #exit_button
    glColor3f(1.0, 0.0, 0.0)
    zone_calc(325, 380, 380, 325)
    zone_calc(380, 380, 325, 325)


def mouseListener(button, state, x, y):
    global l1, flag, p, speed, point

    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            if x >= 20 and y >= 20 and x <= 100 and y <= 75:
                t_x = random.randint(-365, 365)
                l1 = [[t_x, 325], [t_x - 15, 305], [t_x, 285], [t_x + 15, 305]]
                print('Starting over!')
                point = 0
                speed = 0.8
                flag = 1
                p = 1

            if x >= 380 and y >= 20 and x <= 420 and y <= 75:
                if p == 1:
                    p = 0
                else:
                    p = 1

            if x >= 725 and y >= 20 and x <= 780 and y <= 75:
                print('Goodbye! Score:',point)
                glutLeaveMainLoop()

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    if key==GLUT_KEY_RIGHT:
        if l2[3][0] < 380 and p == 1:
            for i in range(len(l2)):
                l2[i][0] += 10
    if key== GLUT_KEY_LEFT:
        if l2[0][0] > -380 and p == 1:
            for i in range(len(l2)):
                l2[i][0] -= 10

    glutPostRedisplay()

def animate():
    glutPostRedisplay()
    if flag == 1 and p == 1:
        diamond_animate()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,401,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    diamond()
    bowl()
    buttons()

    glutSwapBuffers()


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90,	1,	1,	1500)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(50, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)

glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()