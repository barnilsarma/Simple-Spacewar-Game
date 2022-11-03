import pygame                                                                              ##pygame library imported in the program
import sys                                                                                   ##sys library imported in the program   
from math import *
import random
import time
pygame.init()
space=pygame.display.set_mode((600,600))                           ##setting background screen size
pygame.display.set_caption("Spacewar")                                  ##setting game window caption/title
running=False                                                                              ##the variable is set to True while the game loop is running
clock=pygame.time.Clock()                                                        ##setting the clock
points=0
a=0
direction=0
state="stationary"
rocket_x,rocket_y=250,250
x_vel,y_vel=0,0
invaders=[]
n_invaders=10
fired=False
def fire(b_x,b_y,angle):
          global fired,points
          x,y=b_x,b_y
          while(fired==True):
                    pygame.draw.circle(space,(255,255,0),[x,y],2)
                    x+=(-10)*sin(angle)
                    y+=(-10)*cos(angle)
                    if(x<=50 or x>=500 or y<=50 or y>=500):
                              fired=False
                    for invader in invaders:
                              if(distance([x,y],[invader[0],invader[1]])<=10):
                                 points+=1
                                 invader[0],invader[1],invader[2]=random.randint(75,475),random.randint(75,475),random.randint(0,360)
def invader(xpos,ypos,angle):
          pygame.draw.circle(space,(255,50,0),[xpos,ypos],10)
j=0
while(j<n_invaders):
          i_x,i_y,i_a=random.randint(75,475),random.randint(75,475),random.randint(0,360)
          if(i_x<230 or i_x>270):
                    if(i_y<220 or i_y>280):
                              invaders.append([i_x,i_y,i_a*pi/180])
                              j+=1
                    else:
                              continue
##draws the outer boundary of the game
def boundary():                                                                                         
          pygame.draw.rect(space,(255,255,255),[50,50,500,500],10)          ##draws a hollow rectangle
## to show the current score
def score(s):
          f=pygame.font.Font('freesansbold.ttf',25)                                ##defines a font style and size                 
          t=f.render("Score: "+str(s),True,(0,255,0),(0,0,0))                   ##renders the text
          t_rect=t.get_rect()                                                                       ##defines the container of text
          t_rect.center=(400,25)                                                                 ##positioning of text
          space.blit(t,t_rect)                                                                      ##draws the rendered text
def distance(p1,p2):
          return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**(1/2)
##draws the player rocket
r=''
def rocket(xpos,ypos,angle):
          global r
          coords=[
                    [xpos-25*sin(angle),ypos-25*cos(angle)],
                    [xpos+25*sin(angle),ypos+25*cos(angle)]
                    ]
          r=pygame.draw.line(space,(50,50,50),coords[0],coords[1],10)
          front=pygame.draw.line(space,(255,255,255),coords[0],[xpos-25*sin(angle),ypos-25*cos(angle)],10)
def move(b):
          global rocket_x,rocket_y,state,x_vel,y_vel
          if(state=="moving"):
                    x_vel=(-1)*sin(b)
                    y_vel=(-1)*cos(b)
          rocket_x+=x_vel
          rocket_y+=y_vel
##main game function
def game():
          global running,points,a,rocket_x,rocket_y,state,fired         ##global variable 'running'
          global direction
          while(running is True):                                                         ##the loop runs while the variable is True
                    space.fill((0,0,0))                                                                 ##paints the screen with black colour
                    boundary()                                                                  ##calling the boundary function
                    score(points)                                                                   ##calling the score function
                    rocket(rocket_x,rocket_y,a)
                    for child in invaders:
                              invader(child[0],child[1],child[2])
                              if(state=="moving"):
                                        child[0]+=(-1)*sin(child[2])
                                        child[1]+=(-1)*cos(child[2])
                                        if(child[0]<=50):
                                                  child[2]-=pi/2
                                        if(child[0]>=500):
                                                  child[2]+=pi/2
                                        if(child[1]<=50):
                                                  child[2]+=pi/2
                                        if(child[1]>=500):
                                                  child[2]-=pi/2
                                        if(child[0]<=50 and child[1]<=50):
                                                  child[2]-=pi
                                        if(child[0]<=50 and child[1]>=500):
                                                  child[2]+=pi
                                        if(child[0]>=500 and child[1]>=500):
                                                  child[2]+=pi
                                        if(child[0]>=500 and child[1]<=50):
                                                  child[2]-=pi
                                        if(distance([rocket_x-25*sin(a),rocket_y-25*cos(a)],[child[0],child[1]])<=8 or distance([rocket_x,rocket_y],[child[0],child[1]])<=8 or distance([rocket_x+25*sin(a),rocket_y-25*cos(a)],[child[0],child[1]])<=8):
                                                  print("Crashed")
                                                  time.sleep(2)
                                                  running=False
                                                  pygame.quit()
                                                  sys.exit()
                                                  quit()
                    for event in pygame.event.get():                              ##for loop to go through the list of all event types in pygame
                              if(event.type==pygame.QUIT):                      ##QUIT event of pygame
                                        pygame.quit()                                        ##closes all the functions of pygame
                                        sys.exit()                                                ##closes the running window
                                        running=False                                        ##variable set to false to end the while loop
                                        quit()                                                      ##terminates the program
                              if(event.type==pygame.KEYDOWN):
                                        if(event.key==pygame.K_LEFT):         ##Control to rotate anti-clockwise
                                                  if(state=="moving"):
                                                            a+=pi/10
                                        if(event.key==pygame.K_RIGHT):     ##Control to rotate clock-wise
                                                  if(state=="moving"):
                                                            a-=pi/10
                                        if(event.key==pygame.K_UP):
                                                  state="moving"
                                                  direction=a
                                        if(event.key==pygame.K_SPACE):
                                                  fired=True
                                                  fire(rocket_x-25*sin(a),rocket_y-25*cos(a),a)
                    if(rocket_x<=50 or rocket_x>=550 or rocket_y<=50 or rocket_y>=550):
                              print("Crashed")
                              time.sleep(2)
                              running=False
                              pygame.quit()
                              sys.exit()
                              quit()

                    move(direction)
                    pygame.display.update()
                    clock.tick(60)
def intro():
          global running
          while running is False:
                    space.fill((0,0,0))
                    for event in pygame.event.get():
                              if(event.type==pygame.KEYDOWN):
                                        running=True
                                        break
                    f=pygame.font.Font('freesansbold.ttf',25)
                    f2=pygame.font.Font('freesansbold.ttf',15)
                    t1=f.render("GAME CONTROLS:",True,(100,100,255),(0,0,0))
                    t2=f.render("LEFT ARROW KEY   :  To move anti-clockwise",True,(10,200,255),(0,0,0))
                    t3=f.render("RIGHT ARROW KEY  :  To move clockwise",True,(10,200,255),(0,0,0))
                    t4=f.render("UPWARD ARROW KEY  : To move forward ",True,(10,200,255),(0,0,0))
                    t5=f.render("SPACEBAR KEY  :  To shoot",True,(10,200,255),(0,0,0))
                    t6=f2.render("Press any key to Start (except Alt+F4 and close button)",True,(200,10,255),(0,0,0))
                    r1,r2,r3,r4,r5,r6=t1.get_rect(),t2.get_rect(),t3.get_rect(),t4.get_rect(),t5.get_rect(),t6.get_rect()
                    r1.center,r2.center,r3.center,r4.center,r5.center,r6.center=(150,50),(300,100),(300,150),(300,200),(300,250),(300,400)
                    space.blit(t1,r1)
                    space.blit(t2,r2)
                    space.blit(t3,r3)
                    space.blit(t4,r4)
                    space.blit(t5,r5)
                    space.blit(t6,r6)
                    pygame.display.update()
                    clock.tick(60)
intro()                                                                                               ##calling the game intro function
game()                                                                                            ##calling the game function
                                        
          
